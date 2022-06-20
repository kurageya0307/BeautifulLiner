
import os
import sys

                                                                                                                                                                                                                                                                                                            
sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point
from cubic_bezier_control_point import CubicBezierControlPoint
from cubic_bezier_curve import CubicBezierCurve
from part_of_curve import PartOfCurve
from point_sequence import PointSequence
import unittest

class TestPartOfCurve(unittest.TestCase):
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

    def test_init_and_append_using_control_point(self):
        part = PartOfCurve()
        part.set_control_point(self.ctl_p0123)

        ctl_p = part.control_point

        self.assertEqual(ctl_p.p0.x, self.ctl_p0123.p0.x)
    #end

    def test_init_and_append_using_point_sequence(self):
        part = PartOfCurve()
        part.set_point_sequence(self.point_seq)

        points = part.point_sequence.points

        self.assertEqual(points[0].x, self.point_seq.points[0].x)
    #end

    def test_raise_error_appending_as_int(self):
        part = PartOfCurve()
        with self.assertRaises(ValueError) as e:
            part.set_control_point(1)
        #end with
        self.assertEqual(e.exception.args[0], 'appending ctl_p must be CubicBezierControlPoint')

        part = PartOfCurve()
        with self.assertRaises(ValueError) as e:
            part.set_point_sequence(1)
        #end with
        self.assertEqual(e.exception.args[0], 'appending point_seq must be PointSequence')
    #end

    def test_raise_error_in_excluse_using(self):
        part = PartOfCurve()
        part.set_control_point(self.ctl_p0123)
        with self.assertRaises(RuntimeError) as e:
            part.set_point_sequence(self.point_seq)
        #end with
        self.assertEqual(e.exception.args[0], "Exclusion error\nControl point and point sequence cannot be used at the same timecontrol_point")

        part = PartOfCurve()
        part.set_point_sequence(self.point_seq)
        with self.assertRaises(RuntimeError) as e:
            part.set_control_point(self.ctl_p0123)
        #end with
        self.assertEqual(e.exception.args[0], "Exclusion error\nControl point and point sequence cannot be used at the same timecontrol_point")
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

