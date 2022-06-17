
from point import Point
from linear_approximate_curve import LinearApproximateCurve
from typing import List

#                                                                                                                   
#                                                                                                                   
#  Broad linear_approximate curve has 2 lines
#                                                                                                                   
#              O......O.....O......O..                                                        
#           ...       ......O....    ....O.....O...                                           
#        .....O....O..          ...O..            ..O....                                     
#       O...                         ....O.....O..      ..O.....O...                          
#                                                 ..O....          ..O.....O                  
#                                                       ..O.....O....O...  .....              
#                                                                       ....O...O.....O       
#                                                                                     .....O  
#  One is going line
#
#              O......O.....O......O..                                                        
#           ...                      ....O.....O...                                           
#        ...                                      ..O....                                     
#       O.                                              ..O.....O...                          
#                                                                  ..O.....O                  
#                                                                          .....              
#                                                                              .O.....O       
#                                                                                     .....O  
#  The other is returning line
#                             
#                     ......O....                                                             
#           ..O....O..          ...O..                                                        
#       O...                         ....O.....O..                                            
#                                                 ..O....                                     
#                                                       ..O.....O....O...                     
#                                                                       ....O...O.....O       
#                                                                                     .....O  
#  So BroadLinearApproximateCurveSet has two 2d lists of LinearApproximateCurve
#
#  Point                     : One point which has x and y coordinates
#  LinearApproximateCurve    : One cubic Bezier curve approximated with line segmants
#                              It has a list of Point
#  LinearApproximateCurveSet : A set of linear approximated curves
#                              It has a 2d list of LinearApproximateCurve
#                              [ [LinearApproximateCurve in a Layer, curve, curve, ...],  [LinearApproximateCurve in other layer, curve, curve, ...], ... ]
#

class BroadLinearApproximateCurveSet:
    def __init__(self):
        self.__layered_going_curves = []
        self.__layered_returning_curves = []
        self.__group_ids = []
    #end

    def append(self, group_id: str, going_curves: List[LinearApproximateCurve], returning_curves: List[LinearApproximateCurve]):
        if type(group_id) is not str:
            raise ValueError("appending group_id must be str")
        #end if
        if type(going_curves) is not list:
            raise ValueError("appending going_curves must be list")
        #end if
        if type(returning_curves) is not list:
            raise ValueError("appending going_curves must be list")
        #end if
        self.__group_ids.append(group_id)
        self.__layered_going_curves.append(going_curves)
        self.__layered_returning_curves.append(returning_curves)
    #end

    def __iter__(self):
        for group_id, going_curves, returning_curves in zip(self.__group_ids, self.__layered_going_curves, self.__layered_returning_curves):
            yield group_id, going_curves, returning_curves
        #end for
    #end

    def to_svg_str(self):
        s = ""
        #for group_id, curves in zip(self.__group_ids, self.__layered_curves):
        for group_id, going_curves, returning_curves in zip(self.__group_ids, self.__layered_going_curves, self.__layered_returning_curves):
            s += "<g id=\"{}\">\n".format(group_id)
            for going_curve, returning_curve in zip(going_curves, returning_curves):
                s += "<path fill=\"none\" stroke-width=\"1.0\" stroke=\"#000000\" d=\""
                is_first = True
                for point in going_curve.points:
                    if is_first:
                        s += "M {:.3f} {:.3f} ".format(point.x, point.y)
                        is_first = False
                    else:
                        s += "L {:.3f} {:.3f} ".format(point.x, point.y)
                    #end if
                #end for
                for point in returning_curve.points:
                    s += "L {:.3f} {:.3f} ".format(point.x, point.y)
                #end for
                s += "\"/>\n"
            #end for
            s += "</g>"
        #end for
        return s
    #end
#end



