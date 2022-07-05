
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point
from cubic_bezier_control_point import CubicBezierControlPoint
from curve import CubicBezierCurve
from curve import LinearApproximateCurve
from curve_set_in_a_layer import CurveSetInALayer
import unittest

from point_sequence import PointSequence

class TestCurveSetInALayer(unittest.TestCase):
    def setUp(self):
        self.p0 = Point(0.0, 0.0)
        self.p1 = Point(1.0, 2.0)
        self.p2 = Point(10.0, 20.0)
        self.p3 = Point(100.0, 200.0)

        self.ctl_p0123 = CubicBezierControlPoint(self.p0, self.p1, self.p2, self.p3)
        self.ctl_p1230 = CubicBezierControlPoint(self.p1, self.p2, self.p3, self.p0)
    #end

    def test_cubic_bezier_curve_set(self):
        curve = CubicBezierCurve()
        curve.append(self.ctl_p0123)
        curve.append(self.ctl_p1230)

        curve_set = CurveSetInALayer()
        curve_set.append(curve)
        curve_set.append(curve)
        curve_set.append(curve)

        ctl_p = curve_set[0][0]

        self.assertEqual(ctl_p.p0.x, 0.0)
        self.assertEqual(ctl_p.p1.x, 1.0)
    #end

    def test_linear_approximate_curve_set(self):
        curve = LinearApproximateCurve()
        curve.append(self.p0)
        curve.append(self.p1)
        curve.append(self.p2)
        curve.append(self.p3)

        curve_set = CurveSetInALayer()
        curve_set.append(curve)
        curve_set.append(curve)
        curve_set.append(curve)

        p0 = curve_set[0][0]
        p1 = curve_set[0][1]

        self.assertEqual(p0.x, 0.0)
        self.assertEqual(p1.x, 1.0)
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

