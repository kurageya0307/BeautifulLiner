

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

import math
import pprint as pp
import re

from sympy.geometry import *

from curve import LinearApproximateCurve
from curve_set_in_a_layer import CurveSetInALayer
from all_layer_curve_set import AllLayerCurveSet

from numba import jit

RATIO = 0.5

class Segment2:
    def __init__(self, p0, p1):
        self.__x0 = p0.x
        self.__y0 = p0.y
        self.__x1 = p1.x
        self.__y1 = p1.y

        self.__min_x = self.__x0 if self.__x0 < self.__x1 else self.__x1
        self.__max_x = self.__x0 if self.__x0 > self.__x1 else self.__x1
        self.__min_y = self.__y0 if self.__y0 < self.__y1 else self.__y1
        self.__max_y = self.__y0 if self.__y0 > self.__y1 else self.__y1

        self.__center_x = (self.__min_x + self.__max_x)/2.0
        self.__center_y = (self.__min_y + self.__max_y)/2.0

        self.__width  = self.__max_x - self.__min_x
        self.__height = self.__max_y - self.__min_y
    #end

    def intersection(self, other_segment):
        if self.testCollision(other_segment):
            det = (self.__max_x - self.__min_x) * (other_segment.max_y - other_segment.min_y) - (other_segment.max_x - other_segment.min_x) * (self.__max_y - self.__min_y)
            t = ((other_segment.max_y - other_segment.min_y) * (other_segment.max_x - self.__min_x) + (other_segment.min_x - other_segment.max_x) * (other_segment.max_y - self.__min_y)) / det
            x = t * self.__max_x + (1.0 - t) * self.__min_x
            y = t * self.__max_y + (1.0 - t) * self.__min_y
            return [Point(x, y, evaluate=False)]
        #end if
        return []
    #end

    def testCollision(self, other_segment):
        delta_x = abs( other_segment.center_x - self.__center_x )
        delta_y = abs( other_segment.center_y - self.__center_y )

        sum_half_width  = ( other_segment.width  + self.__width  ) / 2.0
        sum_half_height = ( other_segment.height + self.__height ) / 2.0

        if ( (delta_x < sum_half_width) & (delta_y < sum_half_height) ):
            return True
        else:
            return False
        #end if
    #end

    @property
    def max_x(self):
        return self.__max_x
    #end
    @property
    def max_y(self):
        return self.__max_y
    #end
    @property
    def min_x(self):
        return self.__min_x
    #end
    @property
    def min_y(self):
        return self.__min_y
    #end
    @property
    def center_x(self):
        return self.__center_x
    #end
    @property
    def center_y(self):
        return self.__center_y
    #end
    @property
    def width(self):
        return self.__width
    #end
    @property
    def height(self):
        return self.__height
    #end
#end

def getRemoveStartingIndexAndPoint(tip_or_terminal, other_points_sets):
    for target_point_index in range( len(tip_or_terminal)-1 ):
        target_segment = Segment( tip_or_terminal[target_point_index], tip_or_terminal[target_point_index+1], evaluate=False )
        #target_segment = Segment2( tip_or_terminal[target_point_index], tip_or_terminal[target_point_index+1])
        for other_points in other_points_sets:
            for other_point_index in range( len(other_points)-1 ):
                if tip_or_terminal[target_point_index] == other_points[other_point_index]:
                    continue
                if tip_or_terminal[target_point_index+1] == other_points[other_point_index]:
                    continue
                if tip_or_terminal[target_point_index] == other_points[other_point_index+1]:
                    continue
                if tip_or_terminal[target_point_index+1] == other_points[other_point_index+1]:
                    continue
                
                other_segment = Segment( other_points[other_point_index], other_points[other_point_index+1], evaluate=False)
                #other_segment = Segment2( other_points[other_point_index], other_points[other_point_index+1])
                intersect = target_segment.intersection(other_segment)
                if intersect != [] and type(intersect[0]) != Segment2D:
                    ##print(intersect[0])
                    ##print("------------------------------------------------------------------------------------------------------")
                    ##for p in tip_or_terminal:
                    ##    print(p)
                    # and intersect[0] != start_point and intersect[0] != end_point:
                    return target_point_index, intersect[0]
                    #end if
                #end if
            #end
        #end
    #end
    return None, None
#end

def getPointIntersectionOfCurve(linear_approximate_curve, one_curve, space_index):
    split_points, split_rects = one_curve.getSplittedPointsAndRectangulars()

    split_index = 0
    start_split_index = 0
    start_local_index = 0
    start_point = None

    max_check_split_num = math.ceil( len(split_points)*0.3 )
    #print(max_check_split_num)
    #print(len(split_points))
    for points, rect in zip(split_points, split_rects):
        bbox_tupple = (rect.q.x, rect.q.y, rect.m.x, rect.m.y)
        other_points_sets = space_index.intersect(bbox_tupple)

        check_len = len(points)
        for ps in other_points_sets:
            check_len += len(ps)
        #end for

        #print("check_len, {}".format(check_len))
        index, point = getRemoveStartingIndexAndPoint(points, other_points_sets)
        #print("final removed tip : ", point )

        if index is not None:
            start_split_index = split_index
            start_local_index = index
            start_point = point
            break
        #end if
        if split_index >= max_check_split_num:
            break
        #end if
        split_index += 1
    #end for
    #print(start_local_index)

    reverse_split_points = list( reversed(split_points) )
    reverse_split_rects = list( reversed(split_rects) )

    split_index = 0
    end_split_index = len(split_points)
    end_local_index = None
    end_point = None
    for points, rect in zip(reverse_split_points, reverse_split_rects):
        bbox_tupple = (rect.q.x, rect.q.y, rect.m.x, rect.m.y)
        other_points_sets = space_index.intersect(bbox_tupple)

        #print("check_len, {}".format(check_len))
        reverse_points = list( reversed(points) )
        index, point = getRemoveStartingIndexAndPoint(reverse_points, other_points_sets)
        #print("final removed terminal : ", point )

        if index is not None:
            end_split_index = len(split_points) - split_index
            end_local_index = len(points) - index
            end_point = point
            break
        #end if

        if True:#split_index >= max_check_split_num:
            break
        #end if
        split_index += 1
    #end for

    if start_point == end_point:
        return one_curve.points
    #end if
    #print(end_split_index)
    #print(end_local_index)
    #print(end_point)

    removed_points = []
    for i in range(start_split_index, end_split_index):
        points = split_points[i]
        if i == start_split_index:
            if start_point is not None:
                removed_points.append( start_point )
            #end if
            #print(start_local_index)
            for j in range(start_local_index, len(points)):
                removed_points.append( points[j] )
            #end for
        elif i == end_split_index-1:
            end_local_index = len(points) if end_local_index is None else end_local_index
            #print(end_local_index)

            for j in range(0, end_local_index):
                removed_points.append( points[j] )
            #end for
            if end_point is not None:
                removed_points.append( end_point )
            #end if
        else:
            for j in range(0, len(points)):
                removed_points.append( points[j] )
            #end for
        #end if
    #end for
    return removed_points
#end

def removeOverHangs(linear_approximate_curve, space_index):
    all_layer_removed_curves = AllLayerCurveSet()
    total_layer_num = len(linear_approximate_curve)
    layer_index = 0
    for layer_name_one, curve_set_in_one_layer in linear_approximate_curve:
        removed_curve_set = CurveSetInALayer()
        total_curve_num_in_a_layer = len(curve_set_in_one_layer)
        for j, one_curve in enumerate(curve_set_in_one_layer):
            removed_curve = LinearApproximateCurve()
            print("remove edge {}/{} in {} {}/{}".format(j+1, total_curve_num_in_a_layer, layer_name_one, layer_index+1, total_layer_num))
            for point in getPointIntersectionOfCurve(linear_approximate_curve, one_curve, space_index):
                removed_curve.append( point )
            #end for
            removed_curve_set.append(removed_curve)
        #end for
        all_layer_removed_curves.append(layer_name_one, removed_curve_set)
        layer_index += 1
    #end for

    return all_layer_removed_curves
#end