
from point import Point
from linear_approximate_curve import LinearApproximateCurve

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
        if not type(curve) is LinearApproximateCurve:
            raise ValueError("appending curve must be LinearApproximateCurve")

        self.__curves.append(curve)
    #end

    @property
    def curves(self):
        return self.__curves
    #end

    def to_svg_g_str(self, group_id):
        s = ""
        s += "<g id=\"{}\">\n".format(group_id)
        for curve in self.__curves:
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
        return s
    #end
#end



