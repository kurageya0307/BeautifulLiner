
#                                                                                                                   
#                                                                                                                   
#  Broad curve has 2 lines
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
#  So broad curve has two dict of CurveSetInALayer with "layer name" as key
#

from curve_set_in_a_layer import CurveSetInALayer
class BroadAllCurveSet:
    def __init__(self):
        self.__layer_names = []
        self.__going_curve_sets = []
        self.__returning_curve_sets = []
    #end

    def append(self, layer_name : str, going_curve_set : CurveSetInALayer, returning_curve_set : CurveSetInALayer):
        if type(layer_name) is not str:
            raise ValueError("appending layer_name must be str")
        #end if
        if type(going_curve_set) is not CurveSetInALayer:
            raise ValueError("appending going_curve_set must be CurveSetInALayer")
        #end if
        if type(returning_curve_set) is not CurveSetInALayer:
            raise ValueError("appending returning_curve_set must be CurveSetInALayer")
        #end if
        self.__layer_names.append(layer_name)
        self.__going_curve_sets.append(going_curve_set)
        self.__returning_curve_sets.append(returning_curve_set)
    #end

    def __iter__(self):
        for layer_name, going_curve_set, returning_curve_set in zip(self.__layer_names, self.__going_curve_sets, self.__returning_curve_sets):
            yield layer_name, going_curve_set, returning_curve_set
        #end for
    #end

    def to_svg_str(self, color="#000000", shift=0.0):
        s = ""
        #for group_id, curves in zip(self.__group_ids, self.__layered_curves):
        for layer_name, going_curves, returning_curves in zip(self.__layer_names, self.__going_curve_sets, self.__returning_curve_sets):
            s += "<g id=\"{}\" vectornator:layerName=\"{}\">\n".format(layer_name, layer_name)
            for going_curve, returning_curve in zip(going_curves, returning_curves):
                s += "<path fill=\"none\" stroke-width=\"1.0\" stroke=\"" + color + "\" d=\""
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
            s += "</g>\n"
        #end for
        return s
    #end
#end