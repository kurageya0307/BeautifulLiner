
from point import Point

#                                                                                                                   
#                                                                                                                   
#              @@@@@@@@@@@@@@@@@@@@@@@@@                                                                            
#         @@@@@@@@@               @@@@@@@@@@@@@@@@@@@@                                        --+                   
#        @@@                                      @@@@@@@@@@                                    |                   
#       @@                                              @@@@@@@@@@@@@                           |                   
#                                                                  @@@@@@@@@@                   |<- CubicBezierCurve
#                                                                          @@@@@@               |                   
#                                                                              @@@@@@@@@        |                   
#                                                                                     @@@@@@  --+                   
#                       | approximated
#                       V
#                                                                                     
#              O......O.....O......O..                                                                                    --+
#           ...                      ....O.....O...                                           --+                           |
#        ...                                      ..O....                                       |                           |
#       O.                                              ..O.....O...                            |                           |
#                                                                  ..O.....O                    |<- LinearApproximateCurve  |
#                                                                          .....                |                           |
#                                                                              .O.....O         |                           |
#                                                                                     .....O  --+                           |
#              O......O.....O......O..                                                                                      |  <- LinearApproximateCurveSet
#           ...                      ....O.....O...                                           --+                           |
#        ...                                      ..O....                                       |                           |
#       O.                                              ..O.....O...                            |                           |
#                                                                  ..O.....O                    |<- LinearApproximateCurve  |
#                                                                          .....                |                           |
#                                                                              .O.....O         |                           |
#                                                                                     .....O  --+                         --+
#
#  Point                     : One point which has x and y coordinates
#  LinearApproximateCurve    : One cubic Bezier curve approximated with line segmants
#                              It has a list of Point
#  LinearApproximateCurveSet : A set of linear approximated curves
#                              It has a list of LinearApproximateCurve
#

class LinearApproximateCurve:
    def __init__(self):
        self.__points = []
    #end

    def append(self, p):
        if not type(p) is Point:
            raise ValueError("appending p must be Point")

        self.__points.append(p)
    #end

    @property
    def points(self):
        return self.__points
    #end
#end

