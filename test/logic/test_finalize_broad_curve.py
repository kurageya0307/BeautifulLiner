
import os
import sys

from sympy.geometry import *

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))

sys.path.append(os.path.join(os.path.dirname(__file__), '../../logic'))
from finalize_broad_cubic_bezier_curve import *
from broaden_linear_arrpoximate_curve_set import broadenLinearApproximateCurveSet
from delete_overhangs_on_both_edges import deleteOverHangs
from make_segment_space import makeSegmentSpace
from convert_bezier_to_linear_approximate_curve import convertBezierToLinearApproximateCurve
from read_cubic_bezier_curve_from_svg_file import readCubicBezierCurveFromSvgFile

sys.path.append(os.path.join(os.path.dirname(__file__), '../../util'))
from write_svg import *
import unittest

class TestFinalizeBroadCurve(unittest.TestCase):
    def testCreateBroadLinearApproximateCurveSet(self):
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/RemoveEdgeTest.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/NgData.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/KarinFace.svg")
        cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/TaimaninKarin.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/ZeroDivCheck.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/HalfFace.svg")
        linear_approximate_curve = convertBezierToLinearApproximateCurve(cubic_bezier_curve, 1.0, 10)
        diff_str = linear_approximate_curve.to_svg_str(color="#ff0000", shift=0.0)

        segment_space = makeSegmentSpace(linear_approximate_curve, view_box_data)
        all_layer_deleted_curves = deleteOverHangs(linear_approximate_curve, segment_space)
        broad_curve = broadenLinearApproximateCurveSet(all_layer_deleted_curves, 1.0)

        #diff_str += broad_curve.to_svg_str(color="#0000ff")

        final_curve = finalizeBroadCubicBezierCurve(broad_curve)

        writeSvg("hoge.svg", final_curve, color="#008800", shift=1000.0, diff_str=diff_str)
        #print( all_layer_deleted_curves.to_svg_str() )
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end




#end class

if __name__ == '__main__':
    unittest.main()
#end
