
import os
import sys

                                                                                                                                                                                                                                                                                                            
sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point
from linear_approximate_curve import LinearApproximateCurve
import unittest

class TestLinearApproximateCurve(unittest.TestCase):
    def setUp(self):
        p0 = Point(0.0, 0.0)
        p1 = Point(1.0, 2.0)
        p2 = Point(10.0, 20.0)
        p3 = Point(100.0, 200.0)

        self.curve = LinearApproximateCurve()
        self.curve.append(p0)
        self.curve.append(p1)
        self.curve.append(p2)
        self.curve.append(p3)
    #end

    def test_init_and_append(self):
        points = self.curve.points
        self.assertEqual(points[0].to_s(), "0.000,0.000")
        self.assertEqual(points[1].to_s(), "1.000,2.000")
        self.assertEqual(points[2].to_s(), "10.000,20.000")
        self.assertEqual(points[3].to_s(), "100.000,200.000")
    #end

    def test_raise_error_appending_as_int(self):
        self.raise_error_curve = LinearApproximateCurve()
        with self.assertRaises(ValueError) as e:
            self.raise_error_curve.append(1)
        #end with
        self.assertEqual(e.exception.args[0], 'appending p must be Point')
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

