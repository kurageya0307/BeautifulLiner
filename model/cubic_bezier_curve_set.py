
from point import Point
from cubic_bezier_curve import CubicBezierCurve
from typing import List

import numpy as np
#   Point
#   |    
#   V    
#   C                                                                                         --+                    --+  --+
#   @@@@                                                                                        |                      |    |
#      @@@@===                                                                                  |                      |    |
#         @@@========                                                                           |                      |    |
#           @@      =======                                                                @    |                      |    |
#            @@@         ===C                                                            @@@    |                      |    |
#              @@@                                                                      @@@     |                      |    |
#               @@                                                                     @@       |                      |    |
#                @@                                                                   @@        |                      |    |
#                 @@                                                                @@@         |                      |    |
#                  @@                                                              @@           |                      |    |
#                  @@                                                           @@@             |                      |    |
#                    @@                                                        @@@              |<- CubicBezierCurve   |    |
#                     @@                                                     @@@                |                      |    |
#                      @@                                                  @@@                  |                      |    |
#                      @@@                                               @@@                    |                      |    |
#                       @@@                                           @@@@                      |                      |    |
#                         @                                         @@@                         |                      |    |
#                         @@@                                    @@@@@                          |                      |    |
#                           @@                               @@@@@                              |                      |    |
#                            @@@                           @@@@                                 |                      |    |
#                              @@@                    @@@@@@                                    |                      |    |
#                                @@@@@@@@     @@@@@@@@@@                                        |                      |    |
#                                     @@@@@C@@@@                                              --+                      |    |
#                        ===============                                                                               |    |
#                  C=======                                                                                            |    |
#  |                                        |                                                                          |    | <- CubicBezierCurveSet
#  +----------------------------------------+                                                                          |    |
#         A                                                                                                            |    |
#         |                                                                                                            |    |
#    CubicBezierControlPoint                                                                                           |    |
#                                                                                                                      |    |
#                                                                                                                      |    |
#              @@@@@@@@@@@@@@@@@@@@@@@@@                                                                               |    |
#         @@@@@@@@@               @@@@@@@@@@@@@@@@@@@@                                        --+                      |    |
#        @@@                                      @@@@@@@@@@                                    |                      |    |
#       @@                                              @@@@@@@@@@@@@                           |                      |    |
#                                                                  @@@@@@@@@@                   |<- CubicBezierCurve   |    |
#                                                                          @@@@@@               |                      |    |
#                                                                              @@@@@@@@@        |                      |    |
#                                                                                     @@@@@@  --+                    --+    |
#                                                                                                                           |
#                                                                                             --+                    --+    |
#     @@                                                                                        |                      |    |
#      @@@@                                                                                     |                      |    |
#         @@@                                                                                   |                      |    |
#           @@                                                                             @    |<- CubicBezierCurve   |    |
#            @@@                                                                  @@@@@@@@@@    |                      |    |
#              @@@@@@@@@@@@@@@@@@@@@                                @@@@@@@@@@@@@@@@            |                      |    |
#                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          --+                      |    |
#                                                                                                                      |    |
#                                                                                                                      |    |
#              @@@@@@@@@@@@@@@@@@@@@@@@@                                                                               |    |
#         @@@@@@@@@               @@@@@@@@@@@@@@@@@@@@                                        --+                      |    |
#        @@@                                      @@@@@@@@@@                                    |                      |    |
#       @@                                              @@@@@@@@@@@@@                           |                      |    |
#                                                                  @@@@@@@@@@                   |<- CubicBezierCurve   |    |
#                                                                          @@@@@@               |                      |    |
#                                                                              @@@@@@@@@        |                      |    |
#                                                                                     @@@@@@  --+                    --+  --+
#
#  Point                   : One point which has x and y coordinates
#  CubicBezierControlPoint : Control points of a cubic Bezier curve consisting of 4 points.
#                            "C" in the above figure
#  CubicBezierCurve        : One cubic Bezier curve
#                            It has a list of CubicBezierControlPoint
#  CubicBezierCurveSet     : A set of cubic Bezier curves
#                            It has a 2D list of CubicBezierCurve
#                            [ [CubicBezierCurve in a Layer, curve, curve, ...],  [CubicBezierCurve in other layer, curve, curve, ...], ... ]
#

class CubicBezierCurveSet:
    def __init__(self):
        self.__layered_curves = []
        self.__group_ids = []
    #end

    def append(self, group_id: str, curves: List[CubicBezierCurve]):
        if type(group_id) is not str:
            raise ValueError("appending group_id must be str")
        #end if
        if type(curves) is not list:
            raise ValueError("appending curves must be list")
        #end if
        self.__group_ids.append(group_id)
        self.__layered_curves.append(curves)
    #end

    def __iter__(self):
        for group_id, curves in zip(self.__group_ids, self.__layered_curves):
            yield group_id, curves
        #end for
    #end
#end

