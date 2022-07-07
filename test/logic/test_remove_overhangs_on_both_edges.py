import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../logic'))
from remove_overhangs_on_both_edges import *
from convert_bezier_to_linear_approximate_curve import convertBezierToLinearApproximateCurve
from read_cubic_bezier_curve_from_svg_file import readCubicBezierCurveFromSvgFile

import unittest

class TestApproximateCurveWithLineSegments(unittest.TestCase):
    def testConvertBezierToLinearApproximateCurve(self):
        cubic_bezier_curve = readCubicBezierCurveFromSvgFile("data/RemoveEdgeTest.svg")
        linear_approximate_curve = convertBezierToLinearApproximateCurve(cubic_bezier_curve, 5.0)

        all_layer_removed_curves = removeOverHangs(linear_approximate_curve)
        print( all_layer_removed_curves.to_svg_str() )
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

