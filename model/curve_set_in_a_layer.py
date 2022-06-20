
from typing import List
from curve import Curve
class CurveSetInALayer:
    def __init__(self):
        self.__curves = []
    #end

    def append(self, curve: Curve):
        if type(curve) is not Curve:
            raise ValueError("appending curvs must be Curve")
        #end if
        self.__curves.append(curve)
    #end

    def __iter__(self):
        for curve in self.__curves:
            yield curve
        #end for
    #end

    def __getitem__(self, index):
        return self.__curves[index]
    #end

    @property
    def curves(self):
        return self.__curves
    #end

#end