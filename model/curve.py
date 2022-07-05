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
        return Point(max_x, max_y)
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
        return Point(min_x, min_y)
    #end

    def getFullCurveRegionRect(self):
        return Rectangular(self.min(), self.max())
    #end

    def getStartSubRegion(self, ratio):
        """
        ratio is float 0 ~ 1 (Ex. 0.1 = 10%, 0.05 = 5% ...)
        """
        end_index = int( ratio*len(self.__points) )
        return Rectangular( self.min(end_index=end_index), self.max(end_index=end_index) )
    #end

    def getEndSubRegion(self, ratio):
        """
        ratio is float 0 ~ 1 (Ex. 0.1 = 10%, 0.05 = 5% ...)
        """
        start_index = len(self.__points) - int( ratio*len(self.__points) )
        return Rectangular( self.min(start_index=start_index), self.max(start_index=start_index) )
    #end

    def getSegments(self, start_index=0, end_index=None):
        if end_index is None:
            end_index = len( self.__points )
        #end if

        segments = []
        for i in range(start_index, end_index - 1):
            segments.append(  Segment( (self.__points[i].x, self.__points[i].y), (self.__points[i+1].x, self.__points[i+1].y) )  )
        #end for
        return segments
    #end
    
    def getFullSegments(self):
        return self.getSegments()
    #end

    def getStartSegments(self, ratio):
        end_index = int( ratio*len(self.__points) )
        return self.getSegments(end_index=end_index)
    #end

    def getEndSegments(self, ratio):
        start_index = len(self.__points) - int( ratio*len(self.__points) )
        return self.getSegments(start_index=start_index)
    #end


##    def getTenPercenteRectangulars(self):
##        rects = []
##        num_point_sequence = len( self.__parts[0].point_sequence )
##        ten_percent = math.floor( num_point_sequence/10.0 )
##        for i in range(10):
##            start_index = i*ten_percent - 1 if i != 0 else 0
##            end_index   = (i + 1)*ten_percent
##            rects.append(  Rectangular( self.min(start_index, end_index), self.max(start_index, end_index) )  )
##        #end
##        return rects
##    #end

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