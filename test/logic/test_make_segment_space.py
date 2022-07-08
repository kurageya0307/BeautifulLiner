import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../logic'))
from make_segment_space import *
from convert_bezier_to_linear_approximate_curve import convertBezierToLinearApproximateCurve
from read_cubic_bezier_curve_from_svg_file import readCubicBezierCurveFromSvgFile

sys.path.append(os.path.join(os.path.dirname(__file__), '../../util'))
from write_svg import *

import unittest

class TestMakeSegmentSpace(unittest.TestCase):
    def testMakeSegmentSpace(self):
        #cubic_bezier_curve, view_box_data= readCubicBezierCurveFromSvgFile("data/RemoveEdgeTest.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/NgData.svg")
        cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/KarinFace.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/HalfFace.svg")
        linear_approximate_curve = convertBezierToLinearApproximateCurve(cubic_bezier_curve, 1.0, 10)

        segment_space = makeSegmentSpace(linear_approximate_curve, view_box_data)

        print(segment_space)


    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

