
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point
from cubic_bezier_control_point import CubicBezierControlPoint
from curve import Curve
from curve_set_in_a_layer import CurveSetInALayer
from all_curve_set import AllCurveSet
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

    def test_cubic_bezier_curve_set(self):
        part = PartOfCurve()
        part.set_control_point(self.ctl_p0123)

        curve = Curve()
        curve.append(part)
        curve.append(part)
        curve.append(part)

        curve_set = CurveSetInALayer()
        curve_set.append(curve)
        curve_set.append(curve)
        curve_set.append(curve)
        
        all_curve_set = AllCurveSet()
        all_curve_set.append(curve_set)
        all_curve_set.append(curve_set)
        all_curve_set.append(curve_set)
        all_curve_set.append(curve_set)

        ctl_p = all_curve_set[0][0][0].control_point

        self.assertEqual(ctl_p.p0.x, 0.0)
        self.assertEqual(ctl_p.p1.x, 1.0)

        for curve_set_in_a_layer in all_curve_set:
            for curve in curve_set_in_a_layer:
                for part in curve:
                    ctl_p = part.control_point
                    self.assertEqual(ctl_p.p0.x, 0.0)
                    break
                #end for
            #end for
        #end for
    #end

    def test_linear_approximate_curve_set(self):
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

        all_curve_set = AllCurveSet()
        all_curve_set.append(curve_set)
        all_curve_set.append(curve_set)
        all_curve_set.append(curve_set)
        all_curve_set.append(curve_set)

        p_seq = all_curve_set[0][0][0].point_sequence

        self.assertEqual(p_seq[0].x, 0.0)
        self.assertEqual(p_seq[1].x, 1.0)

        for curve_set_in_a_layer in all_curve_set:
            for curve in curve_set_in_a_layer:
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

