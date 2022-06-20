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

from curve_set_in_a_layer import CurveSetInALayer
class AllCurveSet:
    def __init__(self):
        self.__layer_names = []
        self.__curve_sets = []
    #end

    def append(self, layer_name : str, curve_set_in_a_layer : CurveSetInALayer):
        if type(layer_name) is not str:
            raise ValueError("appending layer_name must be str")
        #end if
        if type(curve_set_in_a_layer) is not CurveSetInALayer:
            raise ValueError("appending curve_set_in_a_layer must be CurveSetInALayer")
        #end if
        self.__layer_names.append(layer_name)
        self.__curve_sets.append(curve_set_in_a_layer)
    #end

    def __iter__(self):
        for layer_name, curve_set in zip(self.__layer_names, self.__curve_sets):
            yield layer_name, curve_set
        #end for
    #end

    def __getitem__(self, index):
        return self.__curve_sets[index]
    #end

    @property
    def curves(self):
        return self.__curve_sets
    #end

#end