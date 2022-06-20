
from cubic_bezier_control_point import CubicBezierControlPoint
from point_sequence import PointSequence
class PartOfCurve():
    def __init__(self):
        self.__control_point = None
        self.__point_sequence = None
    #end

    def set_control_point(self, ctl_p):
        if not type(ctl_p) is CubicBezierControlPoint:
            raise ValueError("appending ctl_p must be CubicBezierControlPoint")
        elif self.__point_sequence is not None:
            raise RuntimeError("Exclusion error\nControl point and point sequence cannot be used at the same timecontrol_point")
        #end if
        self.__control_point = ctl_p
    #end

    def set_point_sequence(self, point_seq):
        if not type(point_seq) is PointSequence:
            raise ValueError("appending point_seq must be PointSequence")
        elif self.__control_point is not None:
            raise RuntimeError("Exclusion error\nControl point and point sequence cannot be used at the same timecontrol_point")
        #end if
        self.__point_sequence = point_seq
    #end

    @property
    def control_point(self):
        return self.__control_point
    #end

    @property
    def point_sequence(self):
        return self.__point_sequence
    #end
#end

