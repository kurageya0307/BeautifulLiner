
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

class Point:
    def __init__(self, x, y):
        if not type(x) is float:
            raise ValueError("x must be float")
        if not type(y) is float:
            raise ValueError("y must be float")
        self.__x = x
        self.__y = y
    #end
        
    @property
    def x(self):
        return self.__x
    #end
    @property
    def y(self):
        return self.__y
    #end

    def to_s(self):
        return "{:.3f},{:.3f}".format(self.__x, self.__y)
    #end

#end
