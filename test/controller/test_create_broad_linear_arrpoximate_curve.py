
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point

sys.path.append(os.path.join(os.path.dirname(__file__), '../../controller'))
from create_broad_linear_arrpoximate_curve_set import *
from create_linear_approximate_curve_set import createLinearApproximateCurve
from create_cubic_bezier_curve_set import createCubicBezierCurveSet

import unittest

class TestApproximateCurveWithLineSegments(unittest.TestCase):
    def testGetDeltaPoint(self):
        point_a = Point(0.0, 0.0)
        point_b = Point(10.0, 0.0)
        d_p = getDeltaPoint(point_a, point_b, 1.0)
        self.assertEqual( d_p.to_s(), "10.000,1.000")
    #end def testGetEquallyDividedPointsBetween2Points

    def testGetSlightlyAwayCurve(self):
        points = []
        for i in range(10):
            points.append( Point(float(i*10.0), 0.0) )
        #end

        l = LinearApproximateCurve()
        for point in points:
            l.append(point)
        #end

        slightly_away_curve = getSlightlyAwayCurve(l)

        the_answers = []
        the_answers.append( Point(0.0, 0.0) )
        for i in range(8):
            the_answers.append(   Point(  float( (i + 1)*10.0 ), 1.0  )   )
        #end for
        the_answers.append( Point(90.0, 0.0) )
        for i in range(8):
            the_answers.append(   Point(  float( (8 - i)*10.0 ), -1.0  )   )
        #end for
        the_answers.append( Point(0.0, 0.0) )

        s_points = slightly_away_curve.points
        for i, s_p in enumerate(s_points):
            self.assertEqual( s_p.x, the_answers[i].x )
            self.assertEqual( s_p.y, the_answers[i].y )
#            if i==0:
#                self.assertEqual( s_p.y, 0.0 )
#            elif i==len(s_points)-1:
#                self.assertEqual( s_p.y, 0.0 )
#            else:
#                self.assertEqual( s_p.y, 1.0 )
#            #end if
        #end
    #end

#end class

if __name__ == '__main__':
    unittest.main()
#end
