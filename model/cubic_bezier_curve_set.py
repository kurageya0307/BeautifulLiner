
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

    def to_svg_str(self):
        s = ""
        for group_id, curves in zip(self.__group_ids, self.__layered_curves):
            s += "<g id=\"{}\">\n".format(group_id)
            for curve in curves:
                s += "<path fill=\"#00ff00\" stroke-width=\"1.0\" stroke=\"#none\" d=\""
                is_first = True
                for i, ctl_p in enumerate(curve.control_points):
                    if is_first:
                        s += "M {:.3f} {:.3f} ".format(ctl_p.p0.x, ctl_p.p0.y)
                        s += "C {:.3f} {:.3f} ".format(ctl_p.p1.x, ctl_p.p1.y)
                        s += " {:.3f} {:.3f} ".format(ctl_p.p2.x, ctl_p.p2.y)
                        s += " {:.3f} {:.3f} ".format(ctl_p.p3.x, ctl_p.p3.y)
                        is_first = False
                    else:
                        s += "C {:.3f} {:.3f} ".format(ctl_p.p1.x, ctl_p.p1.y)
                        s += " {:.3f} {:.3f} ".format(ctl_p.p2.x, ctl_p.p2.y)
                        s += " {:.3f} {:.3f} ".format(ctl_p.p3.x, ctl_p.p3.y)
                    #end if
                #end for
                s += "Z \"/>\n"
            #end for
            s += "</g>"
        #end for
        return s
    #end
#end

