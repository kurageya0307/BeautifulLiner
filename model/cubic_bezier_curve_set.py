
from point import Point
from cubic_bezier_curve import CubicBezierCurve

#   Point
#   |    
#   V    
#   C                                                                                         --+                    --+
#   @@@@                                                                                        |                      |
#      @@@@===                                                                                  |                      |
#         @@@========                                                                           |                      |
#           @@      =======                                                                @    |                      |
#            @@@         ===C                                                            @@@    |                      |
#              @@@                                                                      @@@     |                      |
#               @@                                                                     @@       |                      |
#                @@                                                                   @@        |                      |
#                 @@                                                                @@@         |                      |
#                  @@                                                              @@           |                      |
#                   @@                                                           @@@            |                      |
#                    @@                                                        @@@              |<- CubicBezierCurve   |
#                     @@                                                     @@@                |                      |
#                      @@                                                  @@@                  |                      |
#                      @@@                                               @@@                    |                      |
#                       @@@                                           @@@@                      |                      |
#                         @                                         @@@                         |                      |
#                         @@@                                    @@@@@                          |                      |
#                           @@                               @@@@@                              |                      |
#                            @@@                           @@@@                                 |                      |
#                              @@@                    @@@@@@                                    |                      |
#                                @@@@@@@@     @@@@@@@@@@                                        |                      |
#                                     @@@@@C@@@@                                              --+                      |
#                        ===============                                                                               |
#                  C=======                                                                                            |
#  |                                        |                                                                          | <- CubicBezierCurveSet
#  +----------------------------------------+                                                                          |
#         A                                                                                                            |
#         |                                                                                                            |
#    CubicBezierControlPoint                                                                                           |
#                                                                                                                      |
#                                                                                                                      |
#              @@@@@@@@@@@@@@@@@@@@@@@@@                                                                               |
#         @@@@@@@@@               @@@@@@@@@@@@@@@@@@@@                                        --+                      |
#        @@@                                      @@@@@@@@@@                                    |                      |
#       @@                                              @@@@@@@@@@@@@                           |                      |
#                                                                  @@@@@@@@@@                   |<- CubicBezierCurve   |
#                                                                          @@@@@@               |                      |
#                                                                              @@@@@@@@@        |                      |
#                                                                                     @@@@@@  --+                    --+
#
#  Point                   : One point which has x and y coordinates
#  CubicBezierControlPoint : Control points of a cubic Bezier curve consisting of 4 points.
#                            "C" inthe above figure
#  CubicBezierCurve        : One cubic Bezier curve
#                            It has array of CubicBezierControlPoint
#  CubicBezierCurveSet     : A set of cubic Bezier curves
#                            It has array of CubicBezierCurve
#

class CubicBezierCurveSet:
    def __init__(self):
        self.__curves = []
    #end

    def append(self, curve):
        if type(curve) is not CubicBezierCurve:
            raise ValueError("appending curve must be CubicBezierCurve")

        self.__curves.append(curve)
    #end

    @property
    def curves(self):
        return self.__curves
    #end
#end

