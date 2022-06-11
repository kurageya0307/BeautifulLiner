
from point import Point
from linear_approximate_curve import LinearApproximateCurve
from typing import List

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
#              O......O.....O......O..                                                                                    --+  --+
#           ...                      ....O.....O...                                           --+                           |    |
#        ...                                      ..O....                                       |                           |    |
#       O.                                              ..O.....O...                            |                           |    |
#                                                                  ..O.....O                    |<- LinearApproximateCurve  |    |
#                                                                          .....                |                           |    |
#                                                                              .O.....O         |                           |    |
#                                                                                     .....O  --+                           |    |
#              O......O.....O......O..                                                                                      |    |
#           ...                      ....O.....O...                                           --+                           |    |
#        ...                                      ..O....                                       |                           |    |
#       O.                                              ..O.....O...                            |                           |    |
#                                                                  ..O.....O                    |<- LinearApproximateCurve  |    |
#                                                                          .....                |                           |    |
#                                                                              .O.....O         |                           |    |  <- LinearApproximateCurveSet 
#                                                                                     .....O  --+                         --+    |
#                                                                                                                                |
#                                                                                                                                |
#              O......O.....O......O..                                                                                    --+    |
#           ...                      ....O.....O...                                           --+                           |    |
#        ...                                      ..O....                                       |                           |    |
#       O.                                              ..O.....O...                            |                           |    |
#                                                                  ..O.....O                    |<- LinearApproximateCurve  |    |
#                                                                          .....                |                           |    |
#                                                                              .O.....O         |                           |    |
#                                                                                     .....O  --+                           |    |
#              O......O.....O......O..                                                                                      |    |
#           ...                      ....O.....O...                                           --+                           |    |
#        ...                                      ..O....                                       |                           |    |
#       O.                                              ..O.....O...                            |                           |    |
#                                                                  ..O.....O                    |<- LinearApproximateCurve  |    |
#                                                                          .....                |                           |    |
#                                                                              .O.....O         |                           |    |
#                                                                                     .....O  --+                         --+  --+
#
#  Point                     : One point which has x and y coordinates
#  LinearApproximateCurve    : One cubic Bezier curve approximated with line segmants
#                              It has a list of Point
#  LinearApproximateCurveSet : A set of linear approximated curves
#                              It has a 2d list of LinearApproximateCurve
#                              [ [LinearApproximateCurve in a Layer, curve, curve, ...],  [LinearApproximateCurve in other layer, curve, curve, ...], ... ]
#

class LinearApproximateCurveSet:
    def __init__(self):
        self.__layered_curves = []
        self.__group_ids = []
    #end

    def append(self, group_id: str, curves: List[LinearApproximateCurve]):
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

    def to_svg_str(self):
        s = ""
        for group_id, curves in zip(self.__group_ids, self.__layered_curves):
            s += "<g id=\"{}\">\n".format(group_id)
            for curve in curves:
                s += "<path fill=\"none\" stroke-width=\"1.0\" stroke=\"#000000\" d=\""
                is_first = True
                for point in curve.points:
                    if is_first:
                        s += "M {:.3f} {:.3f} ".format(point.x, point.y)
                        is_first = False
                    else:
                        s += "L {:.3f} {:.3f} ".format(point.x, point.y)
                    #end if
                #end for
                s += "\"/>\n"
            #end for
            s += "</g>"
        #end for
        return s
    #end
#end



