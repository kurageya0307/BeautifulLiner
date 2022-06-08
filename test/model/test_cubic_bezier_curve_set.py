
import os
import sys

                                                                                                                                                                                                                                                                                                            
sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point
from cubic_bezier_control_point import CubicBezierControlPoint
from cubic_bezier_curve import CubicBezierCurve
from cubic_bezier_curve_set import CubicBezierCurveSet
import unittest

class TestCubicBezierCurveSet(unittest.TestCase):
    def test_init_and_append(self):
        p0 = Point(0.0, 0.0)
        p1 = Point(1.0, 2.0)
        p2 = Point(10.0, 20.0)
        p3 = Point(100.0, 200.0)

        ctl_p0123 = CubicBezierControlPoint(p0, p1, p2, p3)
        ctl_p1230 = CubicBezierControlPoint(p1, p2, p3, p0)

        curve = CubicBezierCurve()
        curve.append(ctl_p0123)
        curve.append(ctl_p0123)
        #curve.append(ctl_p1230)
        l = [curve, curve]


        self.curve_set = CubicBezierCurveSet()
        self.curve_set.append("a", l)
        self.curve_set.append("b", l)

        the_answer_group_id = ("a", "b")
        the_answer_point = (    (0.0, 0.0),
                                (1.0, 2.0),
                                (10.0, 20.0),
                                (100.0, 200.0) )


        i:int = 0
        for group_id, curves in self.curve_set:
            self.assertEqual(group_id, the_answer_group_id[i])

            for curve in curves:
                j:int = 0
                for j, ctrl_point in enumerate(curve.control_points):
                    if j==0:
                        self.assertEqual(ctrl_point.p0.x, the_answer_point[j][0])
                        self.assertEqual(ctrl_point.p0.y, the_answer_point[j][1])
                    elif j==1:
                        self.assertEqual(ctrl_point.p1.x, the_answer_point[j][0])
                        self.assertEqual(ctrl_point.p1.y, the_answer_point[j][1])
                    elif j==2:
                        self.assertEqual(ctrl_point.p2.x, the_answer_point[j][0])
                        self.assertEqual(ctrl_point.p2.y, the_answer_point[j][1])
                    elif j==3:
                        self.assertEqual(ctrl_point.p3.x, the_answer_point[j][0])
                        self.assertEqual(ctrl_point.p3.y, the_answer_point[j][1])
                    j += 1
                #end for
            #end for
            i += 1
        #end for

    def test_raise_error_appending_as_int(self):
        raise_error_curve_set = CubicBezierCurveSet()
        with self.assertRaises(ValueError) as e:
            raise_error_curve_set.append("a", 1)
        #end with
        self.assertEqual(e.exception.args[0], 'appending curves must be list')
        with self.assertRaises(ValueError) as e:
            raise_error_curve_set.append(1, [1, 2])
        #end with
        self.assertEqual(e.exception.args[0], 'appending group_id must be str')
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

