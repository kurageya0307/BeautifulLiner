
from pyqtree import Index

from sympy.geometry import *

def createRectTuple(p0, p1):
    x0 = p0.x
    y0 = p0.y
    x1 = p1.x
    y1 = p1.y

    min_x = x0 if x0 < x1 else x1
    max_x = x0 if x0 > x1 else x1
    min_y = y0 if y0 < y1 else y1
    max_y = y0 if y0 > y1 else y1

    return (min_x, min_y, max_x, max_y)
#end

def makeSegmentSpace(linear_approximate_curve, view_box_data):
    segment_space = Index(bbox=view_box_data)

    total_layer_num = len(linear_approximate_curve)
    layer_index = 0
    for layer_name_one, curve_set_in_one_layer in linear_approximate_curve:
        total_curve_num_in_a_layer = len(curve_set_in_one_layer)
        for j, curve in enumerate(curve_set_in_one_layer):
            print("make segment space {}/{} in {} {}/{}".format(j+1, total_curve_num_in_a_layer, layer_name_one, layer_index+1, total_layer_num))
            for i in range( len(curve)-1 ):
                segment = Segment( curve[i], curve[i+1], evaluate=False)
                rect_tuple = createRectTuple( curve[i], curve[i+1] )
                segment_space.insert(segment, rect_tuple)
            #end for
        #end for
        layer_index += 1
    #end for

    return segment_space
#end