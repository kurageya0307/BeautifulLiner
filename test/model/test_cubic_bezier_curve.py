
import os
import sys

                                                                                                                                                                                                                                                                                                            
sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point
from cubic_bezier_control_point import CubicBezierControlPoint
from cubic_bezier_curve import CubicBezierCurve
import unittest

class TestCubicBezierCurve(unittest.TestCase):
    def setUp(self):
        p0 = Point(0.0, 0.0)
        p1 = Point(1.0, 2.0)
        p2 = Point(10.0, 20.0)
        p3 = Point(100.0, 200.0)

        ctl_p0123 = CubicBezierControlPoint(p0, p1, p2, p3)
        ctl_p1230 = CubicBezierControlPoint(p1, p2, p3, p0)

        self.curve = CubicBezierCurve()
        self.curve.append(ctl_p0123)
        self.curve.append(ctl_p1230)
    #end

    def test_init_and_append(self):
        ctl_points = self.curve.control_points
        s = ""
        s += "0.000,0.000\n"
        s += "1.000,2.000\n"
        s += "10.000,20.000\n"
        s += "100.000,200.000\n"
        self.assertEqual(ctl_points[0].to_s(),s)

        s = ""
        s += "1.000,2.000\n"
        s += "10.000,20.000\n"
        s += "100.000,200.000\n"
        s += "0.000,0.000\n"
        self.assertEqual(ctl_points[1].to_s(),s)
    #end

    def test_raise_error_appending_as_int(self):
        self.raise_error_curve = CubicBezierCurve()
        with self.assertRaises(ValueError) as e:
            self.raise_error_curve.append(1)
        #end with
        self.assertEqual(e.exception.args[0], 'appending ctl_p must be CubicBezierControlPoint')
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

