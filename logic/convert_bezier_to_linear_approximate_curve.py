
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

from point_sequence import PointSequence
from part_of_curve import PartOfCurve
from curve import Curve
from curve_set_in_a_layer import CurveSetInALayer
from all_curve_set import AllCurveSet
# 
# The Algorithm
#                                                                                                                                        
# 0. Background.
#    Cubic Bezier curve is the point sequence which is calculated by three-step linear interpolation of 4 control points.
#
#    Step 1. Get Q0 ~ Q2 by linear interpolation of 4 control points(P0 ~ P3)
#    Step 2. Get R0 and R1 by linear interpolation of Step1 points(Q0 ~ Q2)
#    Step 3. Get @ by linear interpolation of Step2 points(R0 and R1)
#
#    (More detail, see wikicommons https://commons.wikimedia.org/wiki/File:Bezier_cubic_anim.gif
#     and wikipedia https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
#                                                                                                                                        
#    P1 ...........Q1........................................   P2
#     __          x  ooooo                                         `
#      __        x        ooooooooooR1oooooooooooooooooo           ``
#       _        x            """""""                  oooooooooo    ``
#        _       x        """""     *****************           oooooo Q2 
#         _     x      """""*********               **********           `` 
#          _    x   """" ****                                 ******       `` 
#          _    x ""  @**                                           ******   ``
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
#                                                                                                                                        
#    where P0 ~ P3 are 4 control points of cubic Bezier curve
#          Q0 ~ Q2 are interpolation points of P0 ~ P3
#          R0 ~ R1 are interpolation points of Q0 ~ Q2
#
#          _ : The line between P0 and P1
#          . : The line between P1 and P2
#          ` : The line between P2 and P3
#          x : The line between Q0 and Q1
#          o : The line between Q1 and Q2
#          " : The line between R0 and R1
#
#          @ : The point on cubic Bezier curve at current timing
#
#          * : The final resulting cubic Bezier curve
#                                                                                                                                        
# 1. First, this algorithm computes the Q0 , Q1 and Q2 Points(lists), which are equally divided from P0 to P1 , P1 to P2 and P2 to P3, respectively.         
#                                                                                                                                        
#                                                                                                                                        
#                    Q1 Points
#                  +-----------------------------------------------------------+                                                         
#                  |                                                           |                                                         
#                                                                                                                                        
#                  P1 .....................................................   P2
#             +--   __                                                           `  -------------------------------+
#             |      __                                                          ``                                |
#             |       _                                                            ``                              | Q2 Points
#             |        _                          *****************                  ``                            | 
#  Equally    |         _                 *********               **********           ``                          |
#  divided    |          _             ****                                 ******       ``                        |
#  Q0 Points  |          _          ***                                           ******   ``                      |
#  (list)     |           _       ***                                                  ***** ```                   |
#  on the     |           __     **                                                         *** ``                 |
#  line of    |            _    **                                                            *** ``               |
#  P0 to P1   |             _  **                                                               **  ``             |
#             |             __ *                                                                 **  ``            |
#             |             __ *                                                                  ***  ``          |
#             |               _*                                                                    ***  ```       |
#             |         `     _*                                                                      ***  ``      |
#             |                _*                                                                            P3  --+
#             +--                                                                         
#                              P0                                                        
#                                                                                                                                        
#                                                                                                                                        
#                                                                                                                                        
# 2. Then, it computes the r0 and r1 points from  q0, q1 and q2 , which are the N-th list element of the Q0, Q1 and Q2 Points.
#    r0 and r1 points are also the N-th list element of R0 and R1 Points, which are equally divided from Q0 to Q1 and Q1 to Q2, respectively.     
#
#    It is important to note that r0 and r1 are the N-th elements of the list, as are q0, q1 and q2.
#
#    Since both the "Q0, Q1 and Q2 Points" and "R0 and R1 Points" are point sequences that divide the line segment into equal parts, 
#    the point r0 is the point that divides line q0q1 into |P0q0|:|q0P1|, where |P0q0| is the distance between P0 and q0.
#    The point r1 can be calculated in the same way.
#
#    In other words, it is not necessary to calculate the R0 and R1 lists, and it is sufficient to calculate the internal division point.
#    
#                                                                                                                                        
#    P1 ...........q1........................................   P2
#     __          x  ooooo                                         `
#      __        x        ooooooooor1ooooooooooooooooooo           ``
#       _        x                                     ooooooooo    ``
#        _       x                  *****************           oooooo q2 
#         _     x           *********               **********           `` 
#          _    x        ****                                 ******       `` 
#          _    x     ***                                           ******   ``
#           _   r0  ***                                                  ***** ```
#           __ x   **                                                         *** ``
#            _ x  **                                                            *** ``
#             _x **                                                               **  ``
#             __ *                                                                 **  ``
#             q0 *                                                                  ***  ``
#               _*                                                                    ***  ```
#               _*                                                                      ***  ``
#                _*                                                                            P3
#                                                                           
#                P0                                                        
#                                                                                                                                        
# 3. Finaly, it computes the @ point which is the point that diveded line r0r1 into |P0q0|:|q0P1|
#
#    P1 ...........q1........................................   P2
#     __          x  ooooo                                         `
#      __        x        oooooooooor1oooooooooooooooooo           ``
#       _        x            """""""                  oooooooooo    ``
#        _       x        """""     *****************           oooooo q2 
#         _     x      """""*********               **********           `` 
#          _    x   """" ****                                 ******       `` 
#          _    x ""  @**                                           ******   ``
#           _   r0  ***                                                  ***** ```
#           __ x   **                                                         *** ``
#            _ x  **                                                            *** ``
#             _x **                                                               **  ``
#             __ *                                                                 **  ``
#             q0 *                                                                  ***  ``
#               _*                                                                    ***  ```
#               _*                                                                      ***  ``
#                _*                                                                            P3
#                                                                           
#                P0                                                        
#
# 4. If the division num of Q0, Q1 and Q2 Points is large enough, the resulting point sequence can approximate a cubic Bezier curve with sufficient accuracy.
#


def getDivisionNum(ctrl_p, micro_segment_length):
    vec_p0_p1 = Vector(ctrl_p.p0, ctrl_p.p1)
    vec_p1_p2 = Vector(ctrl_p.p1, ctrl_p.p2)
    vec_p2_p3 = Vector(ctrl_p.p2, ctrl_p.p3)

    length_p0_p1 = vec_p0_p1.abs()
    length_p1_p2 = vec_p1_p2.abs()
    length_p2_p3 = vec_p2_p3.abs()

    division_num_p0_p1 = math.ceil(length_p0_p1 / micro_segment_length)
    division_num_p1_p2 = math.ceil(length_p1_p2 / micro_segment_length)
    division_num_p2_p3 = math.ceil(length_p2_p3 / micro_segment_length)

    return max(division_num_p0_p1, division_num_p1_p2, division_num_p2_p3)
#end def

#
#  point_a                         point_b
#  |                               |
#  V                               V
#
#  A---x---x---x---x---x---x---x---B
#  
#  |                               |
#  +-------------------------------+
#     return_points
#
#   Note!
#     The length of return_points is "division_num + 1"
#
def getEquallyDividedPointsBetween2Points(point_a, point_b, division_num):
    delta_x = (point_b.x - point_a.x) / float(division_num)
    delta_y = (point_b.y - point_a.y) / float(division_num)

    return_points = []
    for i in range(division_num):
        return_points.append(  Point( point_a.x + delta_x*float(i), point_a.y + delta_y*float(i) )  )
    #end
    return_points.append(point_b)

    return return_points
#end def

#
#  point_a                         point_b
#  |                               |
#  V                               V
#
#  A-------@-----------------------B
#     return_point
#  
#  |<----->|<--------------------->|
#      m   :           n
#
#
def getInternalDivisionPoint(point_a, point_b, ratio_m, ratio_n):
    x = ( point_a.x*ratio_n + point_b.x*ratio_m ) / (ratio_m + ratio_n)
    y = ( point_a.y*ratio_n + point_b.y*ratio_m ) / (ratio_m + ratio_n)
    return Point(x, y)
#end def

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
#                     * = return_points
#
def getPointsFromOneCubicBezierCurveSegment(ctrl_p, micro_segment_length):
    division_num = getDivisionNum(ctrl_p, micro_segment_length)

    q0_list = getEquallyDividedPointsBetween2Points(ctrl_p.p0, ctrl_p.p1, division_num)
    q1_list = getEquallyDividedPointsBetween2Points(ctrl_p.p1, ctrl_p.p2, division_num)
    q2_list = getEquallyDividedPointsBetween2Points(ctrl_p.p2, ctrl_p.p3, division_num)

    return_points = []
    for i in range(division_num):
        q0 = q0_list[i]
        q1 = q1_list[i]
        q2 = q2_list[i]

        ratio_n = float(i)
        ratio_m = float(division_num - i)

        r0 = getInternalDivisionPoint(q0, q1, ratio_n, ratio_m)
        r1 = getInternalDivisionPoint(q1, q2, ratio_n, ratio_m)

        return_points.append( getInternalDivisionPoint(r0, r1, ratio_n, ratio_m) )
    #end for

    return return_points
#end def

def convertBezierToLinearApproximateCurve(cubic_bezier_curve, micro_segment_length):
    linear_approximate_curve = AllCurveSet()

    for layer_name, curve_set_in_a_layer in cubic_bezier_curve:
        linear_curve_set = CurveSetInALayer()
        for curve in curve_set_in_a_layer:
            linear_curve = Curve() # linear_curve ??? umm....
            for part in curve:
                ctrl_p = part.control_point
                linear_part = PartOfCurve()
                p_seq = PointSequence()
                for point in getPointsFromOneCubicBezierCurveSegment(ctrl_p, micro_segment_length):
                    p_seq.append(point)
                #end for
                linear_part.set_point_sequence(p_seq)
                linear_curve.append(linear_part)
            #end for
            linear_curve_set.append(linear_curve)
        #end for
        linear_approximate_curve.append(layer_name, linear_curve_set)
    #end for

    return linear_approximate_curve
#end def