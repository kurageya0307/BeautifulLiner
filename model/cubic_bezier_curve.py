
from point import Point
from cubic_bezier_control_point import CubicBezierControlPoint

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

class CubicBezierCurve:
    def __init__(self):
        self.__control_points = []
    #end

    def append(self, ctl_p):
        if not type(ctl_p) is CubicBezierControlPoint:
            raise ValueError("appending ctl_p must be CubicBezierControlPoint")

        self.__control_points.append(ctl_p)
    #end

    @property
    def control_points(self):
        return self.__control_points
    #end
#end

