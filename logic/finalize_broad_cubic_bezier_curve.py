
import numpy as np
from scipy import interpolate
from scipy.interpolate.fitpack import insert
from numpy import asarray, unique, split, sum
from scipy.optimize import curve_fit
from scipy.special import comb

import math
from cubic_bezier_control_point import CubicBezierControlPoint
from curve import CubicBezierCurve
from curve_set_in_a_layer import CurveSetInALayer
from all_layer_curve_set import AllLayerBroadCubicBezierCurveSet

from sympy.geometry import *

def isSimple(curve):
    # reference of curve angle calculated by first 2 points
    x = []
    y = []
    for p in curve:
        x.append(p.x)
        y.append(p.y)
    #end for
    xs = np.array(x)
    ys = np.array(y)
    f_prime = np.gradient(ys)
    indices = np.where(np.diff(np.sign(f_prime)))[0]
    if len(indices) <= 1:
        return True
    else:
        return False
    #end if
    #infections = xs[indices]
#end

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# for simple case
def getBezierParameters(curve):
    """ Least square qbezier fit using penrose pseudoinverse.

    Parameters:

    curve: point sequence which is linear approximate curve of cubic bezier curve

    Based on https://stackoverflow.com/questions/12643079/b%C3%A9zier-curve-fitting-with-scipy
    and probably on the 1998 thesis by Tim Andrew Pastva, "Bezier Curve Fitting".
    """
    degree = 3 # only cubic bezier curve

    x = []
    y = []
    for point in curve:
        x.append(point.x)
        y.append(point.y)
    #end for

    if len(x) < degree + 1:
        x.insert(1, (x[0] + x[1])/2.0 )
        y.insert(1, (y[0] + y[1])/2.0 )
        x.insert(1, (x[0] + x[1])/2.0 )
        y.insert(1, (y[0] + y[1])/2.0 )
        x.insert(1, (x[0] + x[1])/2.0 )
        y.insert(1, (y[0] + y[1])/2.0 )
    #end if
    xdata = np.array(x)
    ydata = np.array(y)
    
    def bpoly(n, t, k):
        """ Bernstein polynomial when a = 0 and b = 1. """
        return t ** k * (1 - t) ** (n - k) * comb(n, k)

    def bmatrix(T):
        """ Bernstein matrix for Bezier curves. """
        return np.matrix([[bpoly(degree, t, k) for k in range(degree + 1)] for t in T])

    def least_square_fit(points, M):
        M_ = np.linalg.pinv(M)
        return M_ * points

    T = np.linspace(0, 1, len(xdata))
    M = bmatrix(T)
    points = np.array(list(zip(xdata, ydata)))

    fit = least_square_fit(points, M).tolist()
    return CubicBezierControlPoint(Point(fit[0][0], fit[0][1], evaluate=False), Point(fit[1][0], fit[1][1], evaluate=False), Point(fit[2][0], fit[2][1], evaluate=False), Point(fit[3][0], fit[3][1], evaluate=False))
#end

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# for complex case
def getComplexCurveCubicBezierPoints(curve):
    x = []
    y = []
    for point in curve:
        x.append( float( point.x ) )
        y.append( float( point.y ) )
    #end for
    xx = np.array(x)
    yy = np.array(y)

    tck,u = interpolate.splprep([xx,yy],s=2.0)
    unew = np.arange(0,1.01,0.01)
    out = interpolate.splev(unew,tck)

    t,c,k = tck
    t = asarray(t)
    try:
        c[0][0]
    except:
        # I can't figure out a simple way to convert nonparametric splines to 
        # parametric splines. Oh well.
        raise TypeError("Only parametric b-splines are supported.")
    #end try

    new_tck = tck
    knots_to_consider = unique(t[k+1:-k-1])

    # For each unique knot, bring it's multiplicity up to the next multiple of k+1
    # This removes all continuity constraints between each of the original knots, 
    # creating a set of independent Bezier curves.
    desired_multiplicity = k+1
    for x in knots_to_consider:
        current_multiplicity = sum(t == x)
        remainder = current_multiplicity%desired_multiplicity
        if remainder != 0:
            # add enough knots to bring the current multiplicity up to the desired multiplicity
            number_to_insert = desired_multiplicity - remainder
            new_tck = insert(x, new_tck, number_to_insert, False)
        #end if
    #end for
    tt,cc,kk = new_tck
    # strip off the last k+1 knots, as they are redundant after knot insertion
    bezier_points = np.transpose(cc)[:-desired_multiplicity]

    # bezier_points is [], it means "Once checked complex, but actually simple". So return simple case control point
    if len(bezier_points) == 0:
        ctrl_p = getBezierParameters(curve)
        return [  [ [ctrl_p.p0.x, ctrl_p.p0.y], [ctrl_p.p1.x, ctrl_p.p1.y], [ctrl_p.p2.x, ctrl_p.p2.y], [ctrl_p.p3.x, ctrl_p.p3.y] ]  ]
    #end if

    # group the points into the desired bezier curves
    return split(bezier_points, len(bezier_points) / desired_multiplicity, axis = 0)
#end 

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# main
def finalizeBroadCubicBezierCurve(broad_curve):
    all_final_curve_set = AllLayerBroadCubicBezierCurveSet()

    total_layer_num = len(broad_curve)
    layer_index = 0
    simple_curve_num = 0
    total_curve_num = 0
    for layer_name, going_curve_set, returning_curve_set in broad_curve:
        total_curve_num_in_a_layer = len(going_curve_set)
        curve_index = 0

        final_going_curve_set = CurveSetInALayer()
        final_returning_curve_set = CurveSetInALayer()
        for going_curve, returning_curve in zip(going_curve_set, returning_curve_set):
            print("finalize {}/{} in {} {}/{}".format(curve_index+1, total_curve_num_in_a_layer, layer_name, layer_index+1, total_layer_num))
            if isSimple(going_curve):
                final_going_curve = CubicBezierCurve()
                final_going_curve.append( getBezierParameters(going_curve) )
                final_going_curve_set.append( final_going_curve )

                final_returning_curve = CubicBezierCurve()
                final_returning_curve.append( getBezierParameters(returning_curve) )
                final_returning_curve_set.append( final_returning_curve )
                simple_curve_num += 1
            else:
                final_going_curve = CubicBezierCurve()
                control_points = getComplexCurveCubicBezierPoints(going_curve)
                for ctrl_p in control_points:
                    final_going_curve.append(  CubicBezierControlPoint( Point(ctrl_p[0][0], ctrl_p[0][1], evaluate=False), 
                                                                        Point(ctrl_p[1][0], ctrl_p[1][1], evaluate=False), 
                                                                        Point(ctrl_p[2][0], ctrl_p[2][1], evaluate=False), 
                                                                        Point(ctrl_p[3][0], ctrl_p[3][1], evaluate=False)  )   )
                #end for
                final_going_curve_set.append( final_going_curve )

                final_returning_curve = CubicBezierCurve()
                control_points = getComplexCurveCubicBezierPoints(returning_curve)
                for ctrl_p in control_points:
                    final_returning_curve.append(  CubicBezierControlPoint( Point(ctrl_p[0][0], ctrl_p[0][1], evaluate=False), 
                                                                            Point(ctrl_p[1][0], ctrl_p[1][1], evaluate=False), 
                                                                            Point(ctrl_p[2][0], ctrl_p[2][1], evaluate=False), 
                                                                            Point(ctrl_p[3][0], ctrl_p[3][1], evaluate=False)  )   )
                #end for
                final_returning_curve_set.append( final_returning_curve )
                pass
            #end if
            total_curve_num += 1
            curve_index += 1
        #end for

        all_final_curve_set.append( layer_name, final_going_curve_set, final_returning_curve_set)
        layer_index += 1
    #end for
    print("simple {}\ntotal {}".format(simple_curve_num, total_curve_num))
    return all_final_curve_set
#end