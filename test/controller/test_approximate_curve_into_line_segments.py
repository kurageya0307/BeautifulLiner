
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point

sys.path.append(os.path.join(os.path.dirname(__file__), '../../controller'))
from approximate_curve_into_line_segments import *
from create_cubic_bezier_curve_set_dict import createCubicBezierCurveSetDict

import unittest

class TestApproximateCurveWithLineSegments(unittest.TestCase):
    def testGetEquallyDividedPointsBetween2Points(self):
        point_a = Point(0.0, 0.0)
        point_b = Point(10.0, 10.0)
        division_num = 10

        points = getEquallyDividedPointsBetween2Points(point_a, point_b, division_num)

        answer = []
        for i in range(division_num):
            answer.append( [float(i), float(i)] )
        #end for
        answer.append( [10.0, 10.0] )

        for i, point in enumerate(points):
            self.assertEqual(point.x, answer[i][0])
            self.assertEqual(point.y, answer[i][1])
            #print( "{}, {}, {}".format(i, point.x, point.y) )
        #end for

    #end def testGetEquallyDividedPointsBetween2Points

    def testGetInternalDivisionPoint(self):
        point_a = Point(1.0, 1.0)
        point_b = Point(10.0, 10.0)

        point = getInternalDivisionPoint(point_a, point_b, 1.0, 2.0)

        answer = [4.0, 4.0]
        self.assertEqual(point.x, answer[0])
        self.assertEqual(point.y, answer[1])
        #print( "{}, {}".format(point.x, point.y) )

    #end def testGetInternalDivisionPoint

    def testConvert(self):
        cubic_bezier_curve_set_dict = createCubicBezierCurveSetDict("data/aaa.svg")
        linear_approximate_curve_set_dict = convert(cubic_bezier_curve_set_dict, 1.0)

        ##print(linear_approximate_curve_set_dict)
        ##for group_id, l_curve_set in linear_approximate_curve_set_dict.items():
        ##    for curve in l_curve_set.curves:
        ##        for point in curve.points:
        ##            print( "[{},{}]".format(point.x, point.y) )
        ##        #end for
        ##    #end for
        ###end for
        for group_id, l_curve_set in linear_approximate_curve_set_dict.items():
            print( l_curve_set.to_svg_g_str(group_id) )
        #end for
            

        pass
    #end deff

#end

#end class

if __name__ == '__main__':
    unittest.main()
#end
