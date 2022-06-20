
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point
from cubic_bezier_control_point import CubicBezierControlPoint
from curve import Curve
from curve_set_in_a_layer import CurveSetInALayer
from all_curve_set import AllCurveSet
from broad_all_curve_set import BroadAllCurveSet
import unittest

from part_of_curve import PartOfCurve
from point_sequence import PointSequence

class TestCubicBezierCurve(unittest.TestCase):
    def setUp(self):
        p0 = Point(0.0, 0.0)
        p1 = Point(1.0, 2.0)
        p2 = Point(10.0, 20.0)
        p3 = Point(100.0, 200.0)

        self.ctl_p0123 = CubicBezierControlPoint(p0, p1, p2, p3)
        self.ctl_p1230 = CubicBezierControlPoint(p1, p2, p3, p0)

        self.point_seq = PointSequence()
        self.point_seq.append(p0)
        self.point_seq.append(p1)
        self.point_seq.append(p2)
        self.point_seq.append(p3)
    #end

    def test_broad_curve_set(self):
        part = PartOfCurve()
        part.set_point_sequence(self.point_seq)

        curve = Curve()
        curve.append(part)
        curve.append(part)
        curve.append(part)

        curve_set = CurveSetInALayer()
        curve_set.append(curve)
        curve_set.append(curve)
        curve_set.append(curve)

        broad_all_curve_set = BroadAllCurveSet()
        broad_all_curve_set.append("layer1", curve_set, curve_set)
        broad_all_curve_set.append("layer2", curve_set, curve_set)
        broad_all_curve_set.append("layer3", curve_set, curve_set)
        broad_all_curve_set.append("layer4", curve_set, curve_set)


        for layer_name, going_curve_set, returning_curve_set in broad_all_curve_set:
            for curve in going_curve_set:
                for part in curve:
                    p_seq = part.point_sequence
                    self.assertEqual(p_seq[0].x, 0.0)
                    break
                #end for
            #end for
            for curve in returning_curve_set:
                for part in curve:
                    p_seq = part.point_sequence
                    self.assertEqual(p_seq[0].x, 0.0)
                    break
                #end for
            #end for
        #end for
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

