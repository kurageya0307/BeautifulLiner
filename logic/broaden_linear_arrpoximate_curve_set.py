

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

import math
import pprint as pp
import re

from sympy.geometry import *

from curve import LinearApproximateCurve
from curve_set_in_a_layer import CurveSetInALayer
from all_layer_curve_set import AllLayerBroadCurveSet

from numba import jit

RATIO = 0.5

from pyqtree import Index
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
    vec_x = current_point.x - prev_point.x
    vec_y = current_point.y - prev_point.y
    len_vec = math.sqrt( vec_x*vec_x + vec_y*vec_y )
    if len_vec == 0:
        return None
    #end if

    final_x = current_point.x - ( vec_y * delta/len_vec)
    final_y = current_point.y + ( vec_x * delta/len_vec)
    return Point(final_x, final_y, evaluate=False)
#end 
def getSlightlyAwayGoingCurve(curve, max_delta):
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

    return the_curve
#end 

def getSlightlyAwayReturningCurve(curve, max_delta):
    the_curve = LinearApproximateCurve()
    points = curve.points

    half_length = len(points)/2.0 - 0.5 

    # first point is equal to original first point
    reversed_points = list( reversed(curve.points) )

    # first point is equal to original first point
    the_curve.append( reversed_points[0] )

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

def makeSlightlyAwayGoingCurves(curves, max_delta):
    return_curves = CurveSetInALayer()
    for curve in curves:
        return_curves.append( getSlightlyAwayGoingCurve(curve, max_delta) )
    #end for
    return return_curves
#end 

def broadenLinearApproximateCurveSet(linear_approximate_curve, max_delta):
    broad_curve = AllLayerBroadCurveSet()
    total_layer_num = len(linear_approximate_curve)
    layer_index = 0
    for layer_name, curve_set in linear_approximate_curve:
        going_broad_curve_set_in_a_layer = CurveSetInALayer()
        returning_broad_curve_set_in_a_layer = CurveSetInALayer()
        total_curve_num_in_a_layer = len(curve_set)
        for j, curve in enumerate(curve_set):
            print("broaden {}/{} in {} {}/{}".format(j+1, total_curve_num_in_a_layer, layer_name, layer_index+1, total_layer_num))
            going_broad_curve_set_in_a_layer.append( getSlightlyAwayReturningCurve(curve, max_delta) )
            returning_broad_curve_set_in_a_layer.append( getSlightlyAwayReturningCurve(curve, max_delta) )
        #end for
        broad_curve.append( layer_name, going_broad_curve_set_in_a_layer, returning_broad_curve_set_in_a_layer )
    #end for
    return broad_curve
#end
