import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../logic'))
from remove_overhangs_on_both_edges import *
from make_segment_space import makeSegmentSpace
from convert_bezier_to_linear_approximate_curve import convertBezierToLinearApproximateCurve
from read_cubic_bezier_curve_from_svg_file import readCubicBezierCurveFromSvgFile

sys.path.append(os.path.join(os.path.dirname(__file__), '../../util'))
from write_svg import *

import unittest

class TestApproximateCurveWithLineSegments(unittest.TestCase):
    def testConvertBezierToLinearApproximateCurve(self):
        cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/RemoveEdgeTest.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/NgData.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/KarinFace.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/TaimaninKarin.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/HalfFace.svg")
        linear_approximate_curve = convertBezierToLinearApproximateCurve(cubic_bezier_curve, 1.0, 10)
        #writeSvg("fuga.svg", linear_approximate_curve, color="#ff0000", diff_str=diff)

        segment_space = makeSegmentSpace(linear_approximate_curve, view_box_data)

        diff_str = linear_approximate_curve.to_svg_str(color="#ff0000")

        all_layer_removed_curves = removeOverHangs(linear_approximate_curve, segment_space)
        writeSvg("hoge.svg", all_layer_removed_curves, color="#008800", shift=0.0, diff_str=diff_str)
#        print( all_layer_removed_curves.to_svg_str() )
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

