
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

        l = [curve, curve]

        self.curve_set = LinearApproximateCurveSet()
        self.curve_set.append("a", l)
        self.curve_set.append("b", l)

        the_answer_point_str = ( ("0.000,0.000"), ("1.000,2.000"), ("10.000,20.000"), ("100.000,200.000") )
        for group_id, curves in self.curve_set:
            for curve in curves:
                for j, point in enumerate(curve.points):
                    self.assertEqual(point.to_s(), the_answer_point_str[j])
                #end for
            #end for
        #end for
    #end

    def test_raise_error_appending_as_int(self):
        self.raise_error_curve_set = LinearApproximateCurveSet()
        with self.assertRaises(ValueError) as e:
            self.raise_error_curve_set.append("a", 1)
        #end with
        self.assertEqual(e.exception.args[0], 'appending curves must be list')
        with self.assertRaises(ValueError) as e:
            self.raise_error_curve_set.append(1, [1, 1])
        #end with
        self.assertEqual(e.exception.args[0], 'appending group_id must be str')
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

