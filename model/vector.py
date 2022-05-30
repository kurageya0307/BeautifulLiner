
import numpy
from point import Point
class Vector:
    def __init__(self, point_a, point_b):
        if not type(point_a) is Point:
            raise ValueError("point_a must be Point")
        if not type(point_b) is Point:
            raise ValueError("point_b must be Point")
        self.__x = point_b.x - point_a.x
        self.__y = point_b.y - point_a.y
    #end
        
    @property
    def x(self):
        return self.__x
    #end
    @property
    def y(self):
        return self.__y
    #end

    def to_s(self):
        return "{:.3f},{:.3f}".format(self.__x, self.__y)
    #end

    def __add__(self, other):
        return Vector( Point(0.0, 0.0), Point(self.__x + other.x, self.__y + other.y ), )
    #end
    def __sub__(self, other):
        return Vector( Point(0.0, 0.0), Point(self.__x - other.x, self.__y - other.y ), )
    #end

    def abs(self):
        return numpy.sqrt( self.__x*self.__x + self.__y*self.__y )
    #end
#end
