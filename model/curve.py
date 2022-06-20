
from part_of_curve import PartOfCurve
class Curve:
    """
    A Curve consists of parts of curve
    """
    def __init__(self):
        self.__parts = []
    #end

    def append(self, part):
        if not type(part) is PartOfCurve:
            raise ValueError("appending part must be PartofCurve")

        self.__parts.append(part)
    #end

    @property
    def parts(self):
        return self.__parts
    #end
#end

