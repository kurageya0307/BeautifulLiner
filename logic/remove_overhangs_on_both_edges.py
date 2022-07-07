

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

import pprint as pp
import re

from sympy.geometry import *

from curve import LinearApproximateCurve
from curve_set_in_a_layer import CurveSetInALayer
from all_layer_curve_set import AllLayerCurveSet

RATIO = 0.5
SPLIT_NUM = 10

def getRemoveStartingIndexAndPoint(tip_or_terminal, other_points_sets):
    hoge = 0
    for target_point_index in range( len(tip_or_terminal)-1 ):
        target_segment = Segment( tip_or_terminal[target_point_index], tip_or_terminal[target_point_index+1], evaluate=False )
        for other_points in other_points_sets:
            for other_point_index in range( len(other_points)-1 ):
                hoge += 1
                other_segment = Segment( other_points[other_point_index], other_points[other_point_index+1], evaluate=False)
                intersect = target_segment.intersection(other_segment)
                if intersect != []:
                    return target_point_index, intersect[0]
                #end if
            #end
        #end
    #end
    return None, None
#end

def getRemovedTipPoints(tip_targets, other_points_sets):
    tip_index, tip_point = getRemoveStartingIndexAndPoint(tip_targets, other_points_sets)

    index_range_after_removed = [ 0, len(tip_targets) ]
    if tip_index is not None:
        index_range_after_removed[0] = tip_index + 1
    #end if

    removed_points = []
    if tip_point is not None:
        removed_points.append(tip_point)
    #end if
    for i in range( index_range_after_removed[0], index_range_after_removed[1] ):
        removed_points.append(tip_targets[i])
    #end for

    return removed_points
#end
def getRemovedTerminalPoints(terminal_targets, other_points_sets):
    terminal_index, terminal_point = getRemoveStartingIndexAndPoint(terminal_targets, other_points_sets)
    #print(terminal_index)

    index_range_after_removed = [ 0, len(terminal_targets) ]
    if terminal_index is not None:
        index_range_after_removed[0] = terminal_index + 1
    #end if

    removed_points = []
    if terminal_point is not None:
        removed_points.append(terminal_point)
    #end if
    for i in range( index_range_after_removed[0], index_range_after_removed[1] ):
        removed_points.append(terminal_targets[i])
    #end for

    removed_points.reverse()

    return removed_points
#end

def getPointIntersectionOfCurve(linear_approximate_curve, one_curve):
    tip_rect = one_curve.getTipSubRegion(RATIO)
    tip_points = one_curve.getTipPoints(RATIO)
    other_points_sets = []
    for layer_name_the_other, curve_set_in_the_other_layer in linear_approximate_curve:
        for the_other_curve in curve_set_in_the_other_layer:
            if one_curve != the_other_curve:
                #print(one_curve)
                split_points, split_rects = the_other_curve.getSplittedPointsAndRectangulars(SPLIT_NUM)
                for points, rect in zip(split_points, split_rects):
                    if rect.testCollision(tip_rect):
                        other_points_sets.append(points)
                    #end if
                #end for
            #end if
        #end for
    #end for
    removed_tip_points = getRemovedTipPoints(tip_points, other_points_sets)

    terminal_rect = one_curve.getTerminalSubRegion(RATIO)
    terminal_points = one_curve.getTerminalPoints(RATIO)
    other_points_sets = []
    for layer_name_the_other, curve_set_in_the_other_layer in linear_approximate_curve:
        for the_other_curve in curve_set_in_the_other_layer:
            if one_curve != the_other_curve:
                #print(one_curve)
                split_points, split_rects = the_other_curve.getSplittedPointsAndRectangulars(SPLIT_NUM)
                for points, rect in zip(split_points, split_rects):
                    if rect.testCollision(terminal_rect):
                        other_points_sets.append(points)
                    #end if
                #end if
            #end if
        #end for
    #end for
    removed_terminal_points = getRemovedTerminalPoints(  list( reversed(terminal_points) ), other_points_sets  )

    middle_points = []#one_curve.getMiddlePoints(RATIO)

    return removed_tip_points + middle_points + removed_terminal_points


#end

def removeOverHangs(linear_approximate_curve):
    all_layer_removed_curves = AllLayerCurveSet()
    total_layer_num = len(linear_approximate_curve)
    for layer_name_one, curve_set_in_one_layer in linear_approximate_curve:
        removed_curve_set = CurveSetInALayer()
        total_curve_num_in_a_layer = len(curve_set_in_one_layer)
        for j, one_curve in enumerate(curve_set_in_one_layer):
            removed_curve = LinearApproximateCurve()
            print("{}/{} in {} {}/{}\n".format(j, total_curve_num_in_a_layer, layer_name_one, 0, total_layer_num))
            for point in getPointIntersectionOfCurve(linear_approximate_curve, one_curve):
                removed_curve.append( point )
            #end for
            removed_curve_set.append(removed_curve)
        #end for
        all_layer_removed_curves.append(layer_name_one, removed_curve_set)
    #end for

    return all_layer_removed_curves
#end