
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

import math
from point import Point
from vector import Vector
from cubic_bezier_control_point import CubicBezierControlPoint
from cubic_bezier_curve import CubicBezierCurve
from cubic_bezier_curve_set import CubicBezierCurveSet

from linear_approximate_curve import LinearApproximateCurve
from linear_approximate_curve_set import LinearApproximateCurveSet

# 
# The Algorithm
#                                                                                                                                        
# 0. Prerequisite
#
#  Cubic Bezier curves are approximated by line segments with approximate_curve_into_line_segments.py
#   
#    P1 ...........Q1........................................   P2
#     __          x  ooooo                                         `
#      __        x        ooooooooooR1oooooooooooooooooo           ``
#       _        x            """""""                  oooooooooo    ``
#        _       x        """""     *****************           oooooo Q2 
#         _     x      """""*********               **********           `` 
#          _    x   """" ****                                 ******       `` 
#          _    x ""  ***                                           ******   ``
#           _   R0  ***                                                  ***** ```
#           __ x   **                                                         *** ``
#            _ x  **                                                            *** ``
#             _x **                                                               **  ``
#             __ *                                                                 **  ``
#             Q0 *                                                                  ***  ``
#               _*                                                                    ***  ```
#               _*                                                                      ***  ``
#                _*                                                                            P3
#                                                                           
#                P0                                                        
#                     * = Points (= Both ends of a line segment)
#
#
#
#
# This module broaden line as below
#
#
#  A ******************************************* B
#
#                     |
#                     V
#
#                    ************       
#            ***************************
#       *************************************
#  A ******************************************* B
#       *************************************
#            ***************************
#                    ************       
#
#
# Line AB consists of multiple line segments
#
#  A o****o******o****o*******o**o****o***o****o B
#
# Now turn attention to the line segments at the first two points
#
#    This! 
#    |
#    V
#    +----+
#    |    |
#  A o****o******o****o*******o**o****o***o****o B
#
# Consider it a vector
#
#  A o---->******o****o*******o**o****o***o****o B
#
# Rotate 90 degrees from the focused vector and find a point slightly away from it.
#
#  A o---->******o****o*******o**o****o***o****o B
#         |
#         V
#         x
#       
# Compute sameway in the second, third ... line segment
#
#  A o---->------>****o*******o**o****o***o****o B
#         |      |    |       |  |    |   |    |
#         V      V    V       V  V    V   V    V
#         x      x    x       x  x    x   x    x
#       
# The distance delta from the original line is a position-dependent function.
# These are small deltas at both ends and large in the center.      
#       
#  A o---->------>****o*******o**o****o***o****o B
#         |      |    |       |  |    |   |    |
#         V      |    |       |  |    |   |    V
#         x      V    V       |  |    V   V    x
#                x    x       V  V    x   x    
#                             x  x
#       
# By calculating this on both sides, a thin line at both ends and a thick line in the center can be obtained.
#       
#       
#                             x  x
#                x    x       A  A    x   x
#         x      A    A       |  |    A   A    x
#         A      |    |       |  |    |   |    A
#         |      |    |       |  |    |   |    |
#  A o****o******o****o*******o**o****o***o****o B
#         |      |    |       |  |    |   |    |
#         V      |    |       |  |    |   |    V
#         x      V    V       |  |    V   V    x
#                x    x       V  V    x   x    
#                             x  x
#       

def getDeltaPoint(prev_point, current_point, delta):
    vec = Vector(prev_point, current_point)
    len_vec = vec.abs()
    if len_vec == 0:
        return None
    #end if

    final_x = current_point.x - ( vec.y * delta/len_vec)
    final_y = current_point.y + ( vec.x * delta/len_vec)
    return Point(final_x, final_y)
#end 
def getSlightlyAwayCurve(curve, max_delta):
    the_curve = LinearApproximateCurve()
    points = curve.points

    half_length = len(points)/2.0 - 0.5 

    # first point is equal to original first point
    the_curve.append( points[0] )

    # middle points are slightly away points
    for i in range( len(points) - 2 ):
        delta = max_delta * ( half_length - abs(half_length - i - 1) ) / half_length
        prev_point = points[i]
        current_point = points[i+1]
        the_point = getDeltaPoint(prev_point, current_point, delta)
        if the_point is not None:
            the_curve.append(the_point)
        #end if
    #end for

    # last point is equal to original last point
    the_curve.append( points[-1] )

    reversed_points = list( reversed(curve.points) )

#    # first point is equal to original first point
#    the_curve.append( reversed_points[0] )

    # middle points are slightly away points
    for i in range( len(reversed_points) - 2 ):
        delta = max_delta * ( half_length - abs(half_length - i - 1) ) / half_length
        prev_point = reversed_points[i]
        current_point = reversed_points[i+1]
        the_point = getDeltaPoint(prev_point, current_point, delta)
        if the_point is not None:
            the_curve.append(the_point)
        #end if
    #end for

    # last point is equal to original last point
    the_curve.append( reversed_points[-1] )

    return the_curve
#end 

def makeSlightlyAwayCurves(curves, max_delta):
    return_curves = []
    for curve in curves:
        return_curves.append( getSlightlyAwayCurve(curve, max_delta) )
    #end for
    return return_curves
#end 

def createBroadLinearApproximateCurveSet(linear_approximate_curve_set, max_delta):
    broad_linear_approximate_curve_set = LinearApproximateCurveSet()
    for group_id, curves in linear_approximate_curve_set:
        broad_linear_approximate_curve_set.append( group_id, makeSlightlyAwayCurves(curves, max_delta) )
    #end for
    return broad_linear_approximate_curve_set
#end
