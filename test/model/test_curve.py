import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from sympy.geometry import *
from cubic_bezier_control_point import CubicBezierControlPoint
from curve import CubicBezierCurve
from curve import LinearApproximateCurve
import unittest

class TestCurve(unittest.TestCase):
    def setUp(self):
        self.p0 = Point(0.0, 0.0)
        self.p1 = Point(1.0, 2.0)
        self.p2 = Point(10.0, 20.0)
        self.p3 = Point(100.0, 200.0)

        self.ctl_p0123 = CubicBezierControlPoint(self.p0, self.p1, self.p2, self.p3)
        self.ctl_p1230 = CubicBezierControlPoint(self.p1, self.p2, self.p3, self.p0)

    #end

    def test_cubic_bezier_curve(self):
        curve = CubicBezierCurve()
        curve.append(self.ctl_p0123)
        curve.append(self.ctl_p1230)

        ctl_p = curve[0]

        self.assertEqual(ctl_p.p0.x, 0.0)
        self.assertEqual(ctl_p.p1.x, 1.0)
    #end

    def test_linear_approximate_curve(self):
        curve = LinearApproximateCurve()
        curve.append(self.p0)
        curve.append(self.p1)
        curve.append(self.p2)
        curve.append(self.p3)

        p0 = curve[0]
        p1 = curve[1]

        self.assertEqual(p0.x, 0.0)
        self.assertEqual(p1.x, 1.0)
    #end

    def test_cllision(self):
        curve1 = LinearApproximateCurve()
        curve2 = LinearApproximateCurve()
        for i in range(40):
            curve1.append(  Point( float(i), float(i) )  )
            curve2.append(  Point( float(i), 6.0 )  )
        #end for

        rect1 = curve1.getFullCurveRegionRect()
        rect2 = curve2.getFullCurveRegionRect()

        self.assertEqual( rect1.q.x, 0.0 )
        self.assertEqual( rect1.q.y, 0.0 )
        self.assertEqual( rect1.m.x, 39.0 )
        self.assertEqual( rect1.m.y, 39.0 )
        self.assertEqual( rect2.q.x, 0.0 )
        self.assertEqual( rect2.q.y, 6.0 )
        self.assertEqual( rect2.m.x, 39.0 )
        self.assertEqual( rect2.m.y, 6.0 )

        self.assertEqual( rect1.testCollision(rect2), True )

    #end

    def test_max_min_rect(self):
        points = []
        for i in range(40):
            points.append(  Point( float(i), float(i) )  )
        #end for

        curve1 = LinearApproximateCurve()
        for p in points:
            curve1.append(p)

        max_p = curve1.max()
        self.assertEqual(max_p.x, 39.0)
        self.assertEqual(max_p.y, 39.0)

        min_p = curve1.min()
        self.assertEqual(min_p.x, 0.0)
        self.assertEqual(min_p.y, 0.0)

        rect = curve1.getFullCurveRegionRect()
        self.assertEqual(rect.q.x, 0.0)
        self.assertEqual(rect.q.y, 0.0)
        self.assertEqual(rect.p.x, 39.0)
        self.assertEqual(rect.p.y, 0.0)
        self.assertEqual(rect.z.x, 0.0)
        self.assertEqual(rect.z.y, 39.0)
        self.assertEqual(rect.m.x, 39.0)
        self.assertEqual(rect.m.y, 39.0)

        min_p_in_5_12 = curve1.min(5, 12)

    #end

    def test_sub_region(self):
        curve1 = LinearApproximateCurve()
        for i in range(40):
            curve1.append(  Point( float(i), float(i) )  )
        #end for

        s_rect = curve1.getStartSubRegion(0.1)
        self.assertEqual(s_rect.q.x, 0.0)
        self.assertEqual(s_rect.q.y, 0.0)
        self.assertEqual(s_rect.m.x, 3.0)
        self.assertEqual(s_rect.m.y, 3.0)

        e_rect = curve1.getEndSubRegion(0.1)
        self.assertEqual(e_rect.q.x, 36.0)
        self.assertEqual(e_rect.q.y, 36.0)
        self.assertEqual(e_rect.m.x, 39.0)
        self.assertEqual(e_rect.m.y, 39.0)
    #end

    def test_segments(self):
        curve1 = LinearApproximateCurve()
        for i in range(40):
            curve1.append(  Point( float(i), float(i) )  )
        #end for

        segments = curve1.getFullSegments()
        self.assertEqual( segments[0].p1.x, 0.0 )
        self.assertEqual( segments[0].p2.x, 1.0 )

        s_segs = curve1.getStartSegments(0.1)
        self.assertEqual( len(s_segs), 3 )

        e_segs = curve1.getEndSegments(0.1)
        self.assertEqual( len(e_segs), 3 )
    #end

#end

if __name__ == '__main__':
    unittest.main()
#end