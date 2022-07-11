
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))

sys.path.append(os.path.join(os.path.dirname(__file__), '../../logic'))
from broaden_linear_arrpoximate_curve_set import *
from delete_overhangs_on_both_edges import deleteOverHangs
from make_segment_space import makeSegmentSpace
from convert_bezier_to_linear_approximate_curve import convertBezierToLinearApproximateCurve
from read_cubic_bezier_curve_from_svg_file import readCubicBezierCurveFromSvgFile

sys.path.append(os.path.join(os.path.dirname(__file__), '../../util'))
from write_svg import *
import unittest

class TestApproximateCurveWithLineSegments(unittest.TestCase):
    def setUp(self):
        self.max_delta = 1.0

        self.points = []
        for i in range(10):
            self.points.append( Point(float(i*10.0), 0.0) )
        #end

        self.l = LinearApproximateCurve()
        for point in self.points:
            self.l.append(point)
        #end

        self.half_length = len(self.points)/2.0 - 0.5 
        self.the_answers = []
        self.the_answers.append( Point(0.0, 0.0) )
        for i in range(8):
            delta = self.max_delta * ( self.half_length - abs(self.half_length - i - 1) ) / self.half_length
            self.the_answers.append(   Point(  float( (i + 1)*10.0 ), delta  )   )
        #end for
        self.the_answers.append( Point(90.0, 0.0) )
        for i in range(8):
            delta = self.max_delta * ( self.half_length - abs(self.half_length - i - 1) ) / self.half_length
            self.the_answers.append(   Point(  float( (8 - i)*10.0 ), -1.0*delta )   )
        #end for
        self.the_answers.append( Point(0.0, 0.0) )
    #end def setUp

    def testGetDeltaPoint(self):
        point_a = Point(0.0, 0.0)
        point_b = Point(10.0, 0.0)
        d_p = getDeltaPoint(point_a, point_b, 1.0)
        self.assertEqual( d_p.x, 10.000)
        self.assertEqual( d_p.y, 1.000)
    #end def testGetEquallyDividedPointsBetween2Points

    def testGetSlightlyAwayGoingCurve(self):
        slightly_away_curve = getSlightlyAwayGoingCurve(self.l, self.max_delta)
        s_points = slightly_away_curve.points
        for i, s_p in enumerate(s_points):
            self.assertAlmostEqual( s_p.x, self.the_answers[i].x )
            self.assertAlmostEqual( s_p.y, self.the_answers[i].y )
        #end
    #end

    def testMakeSlightlyAwayGoingCurves(self):
        slightly_away_curves = makeSlightlyAwayGoingCurves([self.l, self.l, self.l], self.max_delta)
        for slightly_away_curve in slightly_away_curves:
            s_points = slightly_away_curve.points
            for i, s_p in enumerate(s_points):
                self.assertAlmostEqual( s_p.x, self.the_answers[i].x )
                self.assertAlmostEqual( s_p.y, self.the_answers[i].y )
            #end
        #end
    #end

    def testCreateBroadLinearApproximateCurveSet(self):
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/RemoveEdgeTest.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/NgData.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/KarinFace.svg")
        #cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/TaimaninKarin.svg")
        cubic_bezier_curve, view_box_data = readCubicBezierCurveFromSvgFile("data/HalfFace.svg")
        linear_approximate_curve = convertBezierToLinearApproximateCurve(cubic_bezier_curve, 1.0, 10)
        #writeSvg("fuga.svg", linear_approximate_curve, color="#ff0000", diff_str=diff)

        segment_space = makeSegmentSpace(linear_approximate_curve, view_box_data)

        diff_str = linear_approximate_curve.to_svg_str(color="#ff0000")

        all_layer_removed_curves = deleteOverHangs(linear_approximate_curve, segment_space)

        broad_curve = broadenLinearApproximateCurveSet(all_layer_removed_curves, 2.0)


        writeSvg("hoge.svg", broad_curve, color="#008800", shift=0.0, diff_str=diff_str)
#        print( all_layer_removed_curves.to_svg_str() )
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end




#end class

if __name__ == '__main__':
    unittest.main()
#end
