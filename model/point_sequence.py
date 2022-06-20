from point import Point

class PointSequence():
    def __init__(self):
        self.__points = []
    #end

    def append(self, point):
        if not type(point) is Point:
            raise ValueError("appending point must be Point")
        #end if

        self.__points.append(point)
    #end

    @property
    def points(self):
        return self.__points
    #end
#end

