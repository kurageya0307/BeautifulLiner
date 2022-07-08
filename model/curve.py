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

from sympy.geometry import *

from rectangular import Rectangular

import math

from cubic_bezier_control_point import CubicBezierControlPoint

from abc import ABCMeta
from abc import abstractmethod

class Curve(metaclass = ABCMeta):
    @abstractmethod
    def append(self):
        pass
    #end
#end

class CubicBezierCurve(Curve):
    """
    A Curve consists of parts of curve
    """
    def __init__(self):
        self.__control_points = []
    #end

    def append(self, part):
        if not type(part) is CubicBezierControlPoint:
            raise ValueError("appending part must be CubicBezierControlPoint")
        #end
        self.__control_points.append(part)
    #end

    @property
    def control_point(self):
        return self.__control_point
    #end

    def __getitem__(self, index):
        return self.__control_points[index]
    #end
#end

class LinearApproximateCurve(Curve):
    def __init__(self):
        self.__points = []
        self.__split_points = []
        self.__split_rects = []
    #end

    def append(self, point):
        if not type(point) is Point2D:
            raise ValueError("appending part must be Point2D")
        #end
        self.__points.append(point)
    #end

    def max(self, start_index=0, end_index=None):
        if end_index is None:
            end_index = len( self.__points )

        max_x = self.__points[start_index].x
        max_y = self.__points[start_index].y
        for i in range(start_index, end_index):
            p_seq = self.__points[i]
            if p_seq.x > max_x:
                max_x = p_seq.x
            #end if
            if p_seq.y > max_y:
                max_y = p_seq.y
            #end if
        #end for
        return Point(max_x, max_y, evaluate=False)
    #end

    def min(self, start_index=0, end_index=None):
        if end_index is None:
            end_index = len( self.__points )

        min_x = self.__points[start_index].x
        min_y = self.__points[start_index].y
        for i in range(start_index, end_index):
            p_seq = self.__points[i]
            if p_seq.x < min_x:
                min_x = p_seq.x
            #end if
            if p_seq.y < min_y:
                min_y = p_seq.y
            #end if
        #end for
        return Point(min_x, min_y, evaluate=False)
    #end

    def getFullCurveRegionRect(self):
        return Rectangular(self.min(), self.max())
    #end

    def getTipSubRegion(self, ratio):
        """
        ratio is float 0 ~ 1 (Ex. 0.1 = 10%, 0.05 = 5% ...)
        """
        end_index = int( ratio*len(self.__points) )
        return Rectangular( self.min(end_index=end_index), self.max(end_index=end_index) )
    #end

    def getTerminalSubRegion(self, ratio):
        """
        ratio is float 0 ~ 1 (Ex. 0.1 = 10%, 0.05 = 5% ...)
        """
        start_index = len(self.__points) - int( ratio*len(self.__points) )
        return Rectangular( self.min(start_index=start_index), self.max(start_index=start_index) )
    #end

    def getTipPoints(self, ratio):
        end_index = int( ratio*len(self.__points) )
        return self.__points[0:end_index]
    #end

    def getMiddlePoints(self, ratio):
        start_index = int( ratio*len(self.__points) )
        end_index = len(self.__points) - int( ratio*len(self.__points) )
        return self.__points[start_index:end_index]
    #end

    def getTerminalPoints(self, ratio):
        start_index = len(self.__points) - int( ratio*len(self.__points) )
        return self.__points[start_index:-1]
    #end


    def calcSplittedPointsAndRectangulars(self, split_num):
        num_points = len( self.__points )
        percentage = math.floor( num_points / split_num )
        for i in range(split_num):
            start_index = i*percentage - 1 if i != 0 else 0
            end_index   = (i + 1)*percentage if i != (split_num-1) else num_points
            self.__split_points.append( self.__points[start_index:end_index] )
            self.__split_rects.append(  Rectangular( self.min(start_index, end_index), self.max(start_index, end_index) )  )
        #end
    #end

    def getSplittedPointsAndRectangulars(self):
        return self.__split_points, self.__split_rects
    #end

    def getSegment(self, index):
        return Segment( self.__points[index], self.__points[index+1], evaluate=False)
    #end

    def getSegmentRectTuple(self, index):
        x0 = self.__points[index].x
        y0 = self.__points[index].y
        x1 = self.__points[index+1].x
        y1 = self.__points[index+1].y

        min_x = x0 if x0 < x1 else x1
        max_x = x0 if x0 > x1 else x1
        min_y = y0 if y0 < y1 else y1
        max_y = y0 if y0 > y1 else y1

        return (min_x, min_y, max_x, max_y)
    #end

    @property
    def points(self):
        return self.__points
    #end

    def __getitem__(self, index):
        return self.__points[index]
    #end

    def __len__(self):
        return len(self.__points)
    #end
#end