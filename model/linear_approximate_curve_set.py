
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

class LinearApproximateCurveSet:
    def __init__(self):
        self.__curves = []
    #end

    def append(self, curve):
        if not type(p) is LinearApproximateCurve:
            raise ValueError("appending curve must be LinearApproximateCurve")

        self.__curves.append(curve)
    #end

    @property
    def curves(self):
        return self.__curves
    #end
#end

