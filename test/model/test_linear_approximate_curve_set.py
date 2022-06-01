
import os
import sys

                                                                                                                                                                                                                                                                                                            
sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point
from linear_approximate_curve import LinearApproximateCurve
from linear_approximate_curve_set import LinearApproximateCurveSet
import unittest

class TestLinearApproximateCurveSet(unittest.TestCase):
    def setUp(self):
        p0 = Point(0.0, 0.0)
        p1 = Point(1.0, 2.0)
        p2 = Point(10.0, 20.0)
        p3 = Point(100.0, 200.0)

        curve = LinearApproximateCurve()
        curve.append(p0)
        curve.append(p1)
        curve.append(p2)
        curve.append(p3)

        self.curve_set = LinearApproximateCurveSet()
        self.curve_set.append(curve)
        self.curve_set.append(curve)
    #end

    def test_init_and_append(self):
        curves = self.curve_set.curves
        points = curves[0].points
        self.assertEqual(points[0].to_s(), "0.000,0.000")
        self.assertEqual(points[1].to_s(), "1.000,2.000")
        self.assertEqual(points[2].to_s(), "10.000,20.000")
        self.assertEqual(points[3].to_s(), "100.000,200.000")

        points = curves[1].points
        self.assertEqual(points[0].to_s(), "0.000,0.000")
        self.assertEqual(points[1].to_s(), "1.000,2.000")
        self.assertEqual(points[2].to_s(), "10.000,20.000")
        self.assertEqual(points[3].to_s(), "100.000,200.000")
    #end

    def test_raise_error_appending_as_int(self):
        self.raise_error_curve_set = LinearApproximateCurveSet()
        with self.assertRaises(ValueError) as e:
            self.raise_error_curve_set.append(1)
        #end with
        self.assertEqual(e.exception.args[0], 'appending curve must be LinearApproximateCurve')
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

