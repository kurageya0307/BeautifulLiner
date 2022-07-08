import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../logic'))
from remove_overhangs_on_both_edges import *
from convert_bezier_to_linear_approximate_curve import convertBezierToLinearApproximateCurve
from read_cubic_bezier_curve_from_svg_file import readCubicBezierCurveFromSvgFile

sys.path.append(os.path.join(os.path.dirname(__file__), '../../util'))
from write_svg import *

import unittest

class TestApproximateCurveWithLineSegments(unittest.TestCase):
    def testConvertBezierToLinearApproximateCurve(self):
        #cubic_bezier_curve, space_index = readCubicBezierCurveFromSvgFile("data/RemoveEdgeTest.svg")
        diff = ""
        diff += '<g id="Hair" vectornator:layerName="Hair">\n'
        diff += '<path d="M548.062 246.894C548.218 246.794 549.608 250.739 549.667 250.919C550.314 252.87 550.674 254.906 551.093 256.919C552.808 265.178 553.842 274.954 552.041 283.289" fill="none" fill-rule="evenodd" opacity="1" stroke="#1f0a15" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"/>\n'
        diff += '<path d="M559.333 244.804C560.218 249.357 558.701 255.18 557.924 259.668C556.196 269.647 553.156 279.346 548.897 288.514" fill="none" fill-rule="evenodd" opacity="1" stroke="#1f0a15" stroke-linecap="round" stroke-linejoin="round" stroke-width="1"/>\n'
        diff += '</g>\n'

        #cubic_bezier_curve, space_index = readCubicBezierCurveFromSvgFile("data/NgData.svg")
        cubic_bezier_curve, space_index = readCubicBezierCurveFromSvgFile("data/KarinFace.svg")
        #cubic_bezier_curve, space_index = readCubicBezierCurveFromSvgFile("data/HalfFace.svg")
        linear_approximate_curve = convertBezierToLinearApproximateCurve(cubic_bezier_curve, space_index, 1.0, 10)
        #writeSvg("fuga.svg", linear_approximate_curve, color="#ff0000", diff_str=diff)

        diff += linear_approximate_curve.to_svg_str(color="#ff0000")

        all_layer_removed_curves = removeOverHangs(linear_approximate_curve, space_index)
        writeSvg("hoge.svg", all_layer_removed_curves, color="#008800", shift=0.0, diff_str=diff)
#        print( all_layer_removed_curves.to_svg_str() )
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

