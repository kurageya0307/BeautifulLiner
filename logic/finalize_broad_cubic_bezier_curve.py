
import numpy as np
from scipy.optimize import curve_fit
from scipy.special import comb

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
    xdata = np.array(x)
    ydata = np.array(y)
    
    if len(xdata) != len(ydata):
        raise ValueError('xdata and ydata must be of the same length.')

    if len(xdata) < degree + 1:
        raise ValueError(f'There must be at least {degree + 1} points to '
                        f'determine the parameters of a degree {degree} curve. '
                        f'Got only {len(xdata)} points.')

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
                pass
            else:
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