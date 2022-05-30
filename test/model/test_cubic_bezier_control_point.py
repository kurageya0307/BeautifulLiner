
import os
import sys

                                                                                                                                                                                                                                                                                                            
sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point
from cubic_bezier_control_point import CubicBezierControlPoint
import unittest

class TestCubicBezierControlPoint(unittest.TestCase):
    def setUp(self):
        p0 = Point(0.0, 0.0)
        p1 = Point(1.0, 2.0)
        p2 = Point(10.0, 20.0)
        p3 = Point(100.0, 200.0)

        self.ctl_p = CubicBezierControlPoint(p0, p1, p2, p3)
    #end

    def test_init(self):
        s = ""
        s += "0.000,0.000\n"
        s += "1.000,2.000\n"
        s += "10.000,20.000\n"
        s += "100.000,200.000\n"
        self.assertEqual(self.ctl_p.to_s(),s)
    #end

    def test_raise_error_with_set_p0_to_p3_as_int(self):
        p = Point(1.0, 2.1)

        with self.assertRaises(ValueError) as e:
            ctl_p = CubicBezierControlPoint(0, p, p, p)
        #end with
        self.assertEqual(e.exception.args[0], 'p0 must be Point')

        with self.assertRaises(ValueError) as e:
            ctl_p = CubicBezierControlPoint(p, 0, p, p)
        #end with
        self.assertEqual(e.exception.args[0], 'p1 must be Point')

        with self.assertRaises(ValueError) as e:
            ctl_p = CubicBezierControlPoint(p, p, 0, p)
        #end with
        self.assertEqual(e.exception.args[0], 'p2 must be Point')

        with self.assertRaises(ValueError) as e:
            ctl_p = CubicBezierControlPoint(p, p, p, 0)
        #end with
        self.assertEqual(e.exception.args[0], 'p3 must be Point')
    #end

#end

if __name__ == '__main__':
    unittest.main()
#end

