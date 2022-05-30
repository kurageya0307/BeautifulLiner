
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point
from vector import Vector

import unittest

class TestVector(unittest.TestCase):
    def setUp(self):
        p1 = Point(1.0, 2.0)
        p2 = Point(10.0, 20.0)
        p3 = Point(100.0, 200.0)

        self.vec12 = Vector(p1, p2)
        self.vec23 = Vector(p2, p3)
        self.vec12_plus_vec23  = self.vec12 + self.vec23
        self.vec12_minus_vec23 = self.vec12 - self.vec23

    def test_init(self):
        self.assertEqual(self.vec12.to_s(),'9.000,18.000')
        self.assertEqual(self.vec23.to_s(),'90.000,180.000')
    #end

    def test_add(self):
        self.assertEqual(self.vec12_plus_vec23.to_s(),'99.000,198.000')
    #end

    def test_abs(self):
       self.assertAlmostEqual(self.vec12.abs(), 20.12461179749811)
    #end

    def test_add(self):
        self.assertEqual(self.vec12_plus_vec23.to_s(),'99.000,198.000')
    #end

    def test_sub(self):
        self.assertEqual(self.vec12_minus_vec23.to_s(),'-81.000,-162.000')
    #end

    def test_raise_error_with_set_point_a_as_int(self):
        p1 = Point(1.0, 2.0)

        with self.assertRaises(ValueError) as e:
            vec12 = Vector(1, p1)
        #end with
        self.assertEqual(e.exception.args[0], 'point_a must be Point')
    #end

    def test_raise_error_with_set_point_b_as_int(self):
        p1 = Point(1.0, 2.0)

        with self.assertRaises(ValueError) as e:
            vec12 = Vector(p1, 5)
        #end with
        self.assertEqual(e.exception.args[0], 'point_b must be Point')
    #end

#end

if __name__ == '__main__':
    unittest.main()
#end
