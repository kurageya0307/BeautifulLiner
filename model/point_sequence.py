
#   Point
#   |    
#   V    
#   C                                                                                         --+         --+                     --+
#   @@@@                                                                                        |           |                       |
#      @@@@===                                                                                  |           |                       |
#         @@@========                                                                           |           |                       |
#           @@      =======                                                                @    |           |                       |
#            @@@         ===C                                                            @@@    |           |                       |
#              @@@                                                                      @@@     |           |                       |
#               @@                                                                     @@       |           |                       |
#                @@                                                                   @@        |           |                       |
#                 @@                                                                @@@         |           |                       |
#                  @@                                                              @@           |           |                       |
#                  @@                                                           @@@             |           |                       |
#                    @@                                                        @@@              |<- Curve   |                       |
#                     @@                                                     @@@                |           |                       |
#                      @@                                                  @@@                  |           |                       |
#                      @@@                                               @@@                    |           |                       |
#                       @@@                                           @@@@                      |           |                       |
#                         @                                         @@@                         |           |                       |
#                         @@@                                    @@@@@                          |           |                       |
#                           @@                               @@@@@                              |           |                       |
#                            @@@                           @@@@                                 |           |                       |
#                              @@@                    @@@@@@                                    |           |                       |
#                                @@@@@@@@     @@@@@@@@@@                                        |           |                       |
#                                     @@@@@C@@@@                                              --+           |                       |
#                        ===============                                                                    | <- CurveSetInALayer   |
#                  C=======                                                                                 |                       |
#  |                                        |                                                               |                       | <- AllCurveSet
#  +----------------------------------------+                                                               |                       |
#         A                                                                                                 |                       |
#         |                                                                                                 |                       |
#    PartOfCurve                                                                                            |                       |
#                                                                                                           |                       |
#                                                                                                           |                       |
#              @@@@@@@@@@@@@@@@@@@@@@@@@                                                                    |                       |
#         @@@@@@@@@               @@@@@@@@@@@@@@@@@@@@                                        --+           |                       |
#        @@@                                      @@@@@@@@@@                                    |           |                       |
#       @@                                              @@@@@@@@@@@@@                           |           |                       |
#                                                                  @@@@@@@@@@                   |<- Curve   |                       |
#                                                                          @@@@@@               |           |                       |
#                                                                              @@@@@@@@@        |           |                       |
#                                                                                     @@@@@@  --+         --+                       |
#                                                                                                                                   |
#                                                                                             --+         --+                       |
#     @@                                                                                        |           |                       |
#      @@@@                                                                                     |           |                       |
#         @@@                                                                                   |           |                       |
#           @@                                                                             @    |<- Curve   |                       |
#            @@@                                                                  @@@@@@@@@@    |           |                       |
#              @@@@@@@@@@@@@@@@@@@@@                                @@@@@@@@@@@@@@@@            |           |                       |
#                              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                          --+           |                       |
#                                                                                                           | <- CurveSetInALayer   |
#                                                                                                           |                       |
#              @@@@@@@@@@@@@@@@@@@@@@@@@                                                                    |                       |
#         @@@@@@@@@               @@@@@@@@@@@@@@@@@@@@                                        --+           |                       |
#        @@@                                      @@@@@@@@@@                                    |           |                       |
#       @@                                              @@@@@@@@@@@@@                           |           |                       |
#                                                                  @@@@@@@@@@                   |<- Curve   |                       |
#                                                                          @@@@@@               |           |                       |
#                                                                              @@@@@@@@@        |           |                       |
#                                                                                     @@@@@@  --+         --+                     --+
#
#  Point                    : One point which has x and y coordinates
#  PartOfCurve
#   CubicBezierControlPoint : In cubic Bezier curve case
#                             Control points of a cubic Bezier curve consisting of 4 points.
#                             "C" in the above figure
#   PointSequence           : In linear approximate curve case
#                             A point sequence that is finally approximated by the four control points of a cubic Bezier curve
#  Curve                    : One curve
#                             It has a list of PartOfCurve
#  CurveSetInALayer         : A set of curves
#                             It has a list of Curve
#  AllCurveSet              : Layered curve sets in all system
#                             It has a dict of CurveSetInALayer with "layer name" as key
#

from point import Point
class PointSequence():
    def __init__(self):
        self.__points = []
    #end

    def append(self, point):
        if not type(point) is Point:
            raise ValueError("appending point must be Point")
        #end if

        self.__points.append(point)
    #end

    def __getitem__(self, index):
        return self.__points[index]
    #end
#end

