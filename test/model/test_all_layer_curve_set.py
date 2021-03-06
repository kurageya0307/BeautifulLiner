
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from sympy.geometry import *
from cubic_bezier_control_point import CubicBezierControlPoint
from curve import CubicBezierCurve
from curve import LinearApproximateCurve
from curve_set_in_a_layer import CurveSetInALayer
from all_layer_curve_set import *
import unittest

class TestAllLayerCurveSet(unittest.TestCase):
    def setUp(self):
        self.p0 = Point(0.0, 0.0)
        self.p1 = Point(1.0, 2.0)
        self.p2 = Point(10.0, 20.0)
        self.p3 = Point(100.0, 200.0)

        self.ctl_p0123 = CubicBezierControlPoint(self.p0, self.p1, self.p2, self.p3)
        self.ctl_p1230 = CubicBezierControlPoint(self.p1, self.p2, self.p3, self.p0)
    #end

    def test_cubic_bezier_curve_set(self):
        curve = CubicBezierCurve()
        curve.append(self.ctl_p0123)
        curve.append(self.ctl_p1230)

        curve_set = CurveSetInALayer()
        curve_set.append(curve)
        curve_set.append(curve)
        curve_set.append(curve)

        all_curve_set = AllLayerLinearApproximateCurveSet()
        all_curve_set.append("layer1", curve_set)
        all_curve_set.append("layer2", curve_set)
        all_curve_set.append("layer3", curve_set)
        all_curve_set.append("layer4", curve_set)

        ctl_p = all_curve_set[0][0][0]

        self.assertEqual(ctl_p.p0.x, 0.0)
        self.assertEqual(ctl_p.p1.x, 1.0)

        for layer_name, curve_set_in_a_layer in all_curve_set:
            for curve in curve_set_in_a_layer:
                for ctl_p in curve:
                    self.assertEqual(ctl_p.p0.x, 0.0)
                    break
                #end for
            #end for
        #end for
    #end

    def test_linear_approximate_curve_set(self):
        curve = LinearApproximateCurve()
        curve.append(self.p0)
        curve.append(self.p1)
        curve.append(self.p2)
        curve.append(self.p3)

        curve_set = CurveSetInALayer()
        curve_set.append(curve)
        curve_set.append(curve)
        curve_set.append(curve)

        all_curve_set = AllLayerLinearApproximateCurveSet()
        all_curve_set.append("layer1", curve_set)
        all_curve_set.append("layer2", curve_set)
        all_curve_set.append("layer3", curve_set)
        all_curve_set.append("layer4", curve_set)

        p0 = all_curve_set[0][0][0]
        p1 = all_curve_set[0][0][1]

        self.assertEqual(p0.x, 0.0)
        self.assertEqual(p1.x, 1.0)

        for layer_name, curve_set_in_a_layer in all_curve_set:
            for curve in curve_set_in_a_layer:
                for point in curve:
                    self.assertEqual(point.x, 0.0)
                    break
                #end for
            #end for
        #end for
    #end

    def test_broad_curve_set(self):
        curve = LinearApproximateCurve()
        curve.append(self.p0)
        curve.append(self.p1)
        curve.append(self.p2)
        curve.append(self.p3)

        curve_set = CurveSetInALayer()
        curve_set.append(curve)
        curve_set.append(curve)
        curve_set.append(curve)

        broad_all_curve_set = AllLayerBroadCurveSet()
        broad_all_curve_set.append("layer1", curve_set, curve_set)
        broad_all_curve_set.append("layer2", curve_set, curve_set)
        broad_all_curve_set.append("layer3", curve_set, curve_set)
        broad_all_curve_set.append("layer4", curve_set, curve_set)


        for layer_name, going_curve_set, returning_curve_set in broad_all_curve_set:
            for curve in going_curve_set:
                for p in curve:
                    self.assertEqual(p.x, 0.0)
                    break
                #end for
            #end for
            for curve in returning_curve_set:
                for p in curve:
                    self.assertEqual(p.x, 0.0)
                    break
                #end for
            #end for
        #end for
    #end
#end

if __name__ == '__main__':
    unittest.main()
#end

