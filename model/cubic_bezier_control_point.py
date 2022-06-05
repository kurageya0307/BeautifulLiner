
from point import Point

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

class CubicBezierControlPoint:
    def __init__(self, p0, p1, p2, p3):
        if not type(p0) is Point:
            raise ValueError("p0 must be Point")
        if not type(p1) is Point:
            raise ValueError("p1 must be Point")
        if not type(p2) is Point:
            raise ValueError("p2 must be Point")
        if not type(p3) is Point:
            raise ValueError("p3 must be Point")

        self.__p0 = Point(p0.x, p0.y)
        self.__p1 = Point(p1.x, p1.y)
        self.__p2 = Point(p2.x, p2.y)
        self.__p3 = Point(p3.x, p3.y)
    #end

    @property
    def p0(self):
        return self.__p0
    #end def

    @property
    def p1(self):
        return self.__p1
    #end def

    @property
    def p2(self):
        return self.__p2
    #end def

    @property
    def p3(self):
        return self.__p3
    #end def

    def to_s(self):
        s = ""
        s += self.__p0.to_s() + "\n"
        s += self.__p1.to_s() + "\n"
        s += self.__p2.to_s() + "\n"
        s += self.__p3.to_s() + "\n"
        return s
    #end
#end

