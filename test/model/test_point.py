
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point

import unittest

class TestPoint(unittest.TestCase):
    def test_to_s(self):
        p = Point(10.1, 11.2)
        self.assertEqual(p.to_s(), '10.100,11.200')
    #end

    def test_raise_error_with_set_x_as_int(self):
        with self.assertRaises(ValueError) as e:
            p = Point(1, 2.1)
        #end with
        self.assertEqual(e.exception.args[0], 'x must be float')
    #end

    def test_raise_error_with_set_y_as_int(self):
        with self.assertRaises(ValueError) as e:
            p = Point(1.23, 2)
        #end with
        self.assertEqual(e.exception.args[0], 'y must be float')
    #end

#end class

if __name__ == '__main__':
    unittest.main()
#end if
