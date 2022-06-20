

from curve_set_in_a_layer import CurveSetInALayer
class AllCurveSet:
    def __init__(self):
        self.__curve_sets = []
    #end

    def append(self, curve_set_in_a_layer: CurveSetInALayer):
        if type(curve_set_in_a_layer) is not CurveSetInALayer:
            raise ValueError("appending curve_set_in_a_layer must be CurveSetInALayer")
        #end if
        self.__curve_sets.append(curve_set_in_a_layer)
    #end

    def __iter__(self):
        for curve_set in self.__curve_sets:
            yield curve_set
        #end for
    #end

    def __getitem__(self, index):
        return self.__curve_sets[index]
    #end

    @property
    def curves(self):
        return self.__curve_sets
    #end

#end