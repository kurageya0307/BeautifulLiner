
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

from cubic_bezier_control_point import CubicBezierControlPoint
from cubic_bezier_curve import CubicBezierCurve
from cubic_bezier_curve_set import CubicBezierCurveSet

# 
# The Algorithm
#                                                                                                                                        
# 1. Cubic Bezier curve is the point sequence which is calculated by three-step linear interpolation of 4 control points.
#
#    Step 1. Get M0 ~ M2 by linear interpolation of 4 control points(P0 ~ P3)
#    Step 2. Get B0 and B1 by linear interpolation of Step1 points(M0 ~ M2)
#    Step 3. Get @ by linear interpolation of Step2 points(B0 and B1)
#
#    (More detail, see wikicommons https://commons.wikimedia.org/wiki/File:Bezier_cubic_anim.gif
#     and wikipedia https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
#                                                                                                                                        
#    P1 ...........M1........................................   P2
#     __          x  ooooo                                         `
#      __        x        ooooooooooB1oooooooooooooooooo           ``
#       _        x            """""""                  oooooooooo    ``
#        _       x        """""     *****************           oooooo M2 
#         _     x      """""*********               **********           `` 
#          _    x   """" ****                                 ******       `` 
#          _    x ""  @**                                           ******   ``
#           _   B0  ***                                                  ***** ```
#           __ x   **                                                         *** ``
#            _ x  **                                                            *** ``
#             _x **                                                               **  ``
#             __ *                                                                 **  ``
#             M0 *                                                                  ***  ``
#               _*                                                                    ***  ```
#               _*                                                                      ***  ``
#                _*                                                                            P3
#                                                                           
#                P0                                                        
#                                                                                                                                        
#    where P0 ~ P3 are 4 control points of cubic Bezier curve
#          M0 ~ M2 are interpolation points of P0 ~ P3
#          B0 ~ B1 are interpolation points of M0 ~ M2
#
#          _ : The line between P0 and P1
#          . : The line between P1 and P2
#          ` : The line between P2 and P3
#          x : The line between M0 and M1
#          o : The line between M1 and M2
#          " : The line between B0 and B1
#
#          @ : The point on cubic Bezier curve at this timing
#
#          * : The final resulting cubic Bezier curve
#                                                                                                                                        
# 2. First, this algorithm computes the M0 , M1 and M2 Points(lists), which are equally divided from P0 to P1 , P1 to P2 and P2 to P3, respectively.         
#                                                                                                                                        
#                                                                                                                                        
#                    M1 Points
#                  +-----------------------------------------------------------+                                                         
#                  |                                                           |                                                         
#                                                                                                                                        
#                  P1 .....................................................   P2
#             +--   __                                                           `  -------------------------------+
#             |      __                                                          ``                                |
#             |       _                                                            ``                              | M2 Points
#             |        _                          *****************                  ``                            | 
#  Equally    |         _                 *********               **********           ``                          |
#  divided    |          _             ****                                 ******       ``                        |
#  M0 Points  |          _          ***                                           ******   ``                      |
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
# 3. Then, it computes the b0 and b1 points from  m0, m1 and m2 , which are the N-th list element of the M0, M1 and M2 Points.
#    b0 and b1 points are also the N-th list element of B0 and B1 Points, which are equally divided from M0 to M1 and M1 to M2, respectively.     
#
#    It is important to note that b0 and b1 are the N-th elements of the list, as are m0, m1 and m2.
#
#    Since both the "M0, M1 and M2 Points" and "B0 and B1 Points" are point sequences that divide the line segment into equal parts, 
#    the point b0 is the point that divides line m0m1 into |P0m0|:|m0P1|, where |P0m0| is the distance between P0 and m0.
#    The point b1 can be calculated in the same way.
#
#    In other words, it is not necessary to calculate the B0 and B1 lists, and it is sufficient to calculate the Internal division point.
#    
#                                                                                                                                        
#    P1 ...........m1........................................   P2
#     __          x  ooooo                                         `
#      __        x        ooooooooob1ooooooooooooooooooo           ``
#       _        x                                     oooooooooo    ``
#        _       x                  *****************           oooooo m2 
#         _     x           *********               **********           `` 
#          _    x        ****                                 ******       `` 
#          _    x     ***                                           ******   ``
#           _   b0  ***                                                  ***** ```
#           __ x   **                                                         *** ``
#            _ x  **                                                            *** ``
#             _x **                                                               **  ``
#             __ *                                                                 **  ``
#             m0 *                                                                  ***  ``
#               _*                                                                    ***  ```
#               _*                                                                      ***  ``
#                _*                                                                            P3
#                                                                           
#                P0                                                        
#                                                                                                                                        
# 4. Finaly, it computes the @ point which is the point that diveded line b0b1 into |P0m0|:|m0P1|
#
#    P1 ...........m1........................................   P2
#     __          x  ooooo                                         `
#      __        x        oooooooooob1oooooooooooooooooo           ``
#       _        x            """""""                  oooooooooo    ``
#        _       x        """""     *****************           oooooo m2 
#         _     x      """""*********               **********           `` 
#          _    x   """" ****                                 ******       `` 
#          _    x ""  @**                                           ******   ``
#           _   b0  ***                                                  ***** ```
#           __ x   **                                                         *** ``
#            _ x  **                                                            *** ``
#             _x **                                                               **  ``
#             __ *                                                                 **  ``
#             m0 *                                                                  ***  ``
#               _*                                                                    ***  ```
#               _*                                                                      ***  ``
#                _*                                                                            P3
#                                                                           
#                P0                                                        
#
# 5. If the division num of M0, M1 and M2 Points is large enough, the resulting point sequence can approximate a cubic Bezier curve with sufficient accuracy.
#
