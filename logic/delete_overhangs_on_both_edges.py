

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

import math
import pprint as pp
import re

from sympy.geometry import *

from curve import LinearApproximateCurve
from curve_set_in_a_layer import CurveSetInALayer
from all_layer_curve_set import AllLayerLinearApproximateCurveSet

from numba import jit

RATIO = 0.5

from pyqtree import Index

def getEdgeDeletedCurve(curve, segment_space, ratio):
    deleted_curve = LinearApproximateCurve()
    for p in curve:
        deleted_curve.append(p)
    #end for

    intersect_points = []
    intersect_indexes = []
    for i in range( len(curve)-1 ):
        the_segment = curve.getSegment(i)
        the_segment_rect = curve.getSegmentRectTuple(i)
        other_segments = segment_space.intersect(the_segment_rect)
        for other_segment in other_segments:
            if type(the_segment) == Point2D:
                continue
            if type(other_segment) == Point2D:
                continue
            if the_segment == other_segment:
                continue
            if (the_segment.p1==other_segment.p2):
                continue
            if (the_segment.p2==other_segment.p1):
                continue
                
            inter = the_segment.intersection(other_segment)
            if inter != [] and type(inter[0]) != Segment2D:
                intersect_points.append(inter[0])
                intersect_indexes.append(i)
            #end if
        #end
    #end

    if len(intersect_points) == 0:
        deleted_curve.setStartIndex(0)
        deleted_curve.setEndIndex( len(deleted_curve) )
        return deleted_curve
    elif len(intersect_points) == 1:
        dist_start_intersect = curve[0].distance(intersect_points[0])
        dist_end_intersect   = curve[-1].distance(intersect_points[0])
        dist_start_end       = curve[0].distance(curve[-1])

        #if (dist_start_end*0.3 > dist_start_intersect) and (dist_start_end*0.3 > dist_end_intersect):
        #    return curve
        ##endif
        #not work ummm...

        if dist_start_intersect < dist_end_intersect:
            deleted_curve.setStartIndex( intersect_indexes[0] )
            deleted_curve.setEndIndex( len(deleted_curve) )
            return deleted_curve
        else:
            deleted_curve.setStartIndex( 0 )
            deleted_curve.setEndIndex( intersect_indexes[0] )
            return deleted_curve
        #end if
    else:
        start_index = 0
        end_index = len(curve)
        total_point_num = len(curve)

        if (intersect_indexes[0]/total_point_num) < ratio:
            start_index = intersect_indexes[0]
        #end if
        if ( (total_point_num - intersect_indexes[-1])/total_point_num ) < ratio:
            end_index = intersect_indexes[-1] + 1
        #end if
        deleted_curve.setStartIndex( start_index )
        deleted_curve.setEndIndex( end_index )
        return deleted_curve
    #end if
#end


def deleteOverHangs(linear_approximate_curve, segment_space, ratio):
    all_layer_deleted_curves = AllLayerLinearApproximateCurveSet()
    total_layer_num = len(linear_approximate_curve)
    layer_index = 0
    for layer_name_one, curve_set_in_one_layer in linear_approximate_curve:
        deleted_curve_set = CurveSetInALayer()
        total_curve_num_in_a_layer = len(curve_set_in_one_layer)
        for j, curve in enumerate(curve_set_in_one_layer):
            print("delete edge {}/{} in {} {}/{}".format(j+1, total_curve_num_in_a_layer, layer_name_one, layer_index+1, total_layer_num))
            deleted_curve = getEdgeDeletedCurve(curve, segment_space, ratio)
            deleted_curve_set.append(deleted_curve)
        #end for
        all_layer_deleted_curves.append(layer_name_one, deleted_curve_set)
        layer_index += 1
    #end for

    return all_layer_deleted_curves
#end