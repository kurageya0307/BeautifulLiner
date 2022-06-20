

from curve_set_in_a_layer import CurveSetInALayer
class AllCurveSet:
    def __init__(self):
        self.__layer_names = []
        self.__curve_sets = []
    #end

    def append(self, layer_name : str, curve_set_in_a_layer : CurveSetInALayer):
        if type(layer_name) is not str:
            raise ValueError("appending layer_name must be str")
        #end if
        if type(curve_set_in_a_layer) is not CurveSetInALayer:
            raise ValueError("appending curve_set_in_a_layer must be CurveSetInALayer")
        #end if
        self.__layer_names.append(layer_name)
        self.__curve_sets.append(curve_set_in_a_layer)
    #end

    def __iter__(self):
        for layer_name, curve_set in zip(self.__layer_names, self.__curve_sets):
            yield layer_name, curve_set
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