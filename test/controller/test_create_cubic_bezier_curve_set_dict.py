
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../controller'))
from create_cubic_bezier_curve_set_group import *

import unittest

class TestCreateCubicBezierCurveSetGroup(unittest.TestCase):
    def testMakeCubicBezierCurve(self):
        d_str = 'M624.369 665.275C624.369 665.275 615.909 650.653 610.912 630.454C605.916 610.254 602.648 598.519 602.648 598.519L599.189 586.015'
        curve = makeCubicBezierCurve(d_str)
        ctl_points = curve.control_points

        s = ""
        s += "624.369,665.275\n"
        s += "624.369,665.275\n"
        s += "615.909,650.653\n"
        s += "610.912,630.454\n"
        self.assertEqual(ctl_points[0].to_s(),s)

        s = ""
        s += "610.912,630.454\n"
        s += "605.916,610.254\n"
        s += "602.648,598.519\n"
        s += "602.648,598.519\n"
        self.assertEqual(ctl_points[1].to_s(),s)

        s = ""
        s += "602.648,598.519\n"
        s += "600.918,592.267\n"
        s += "600.918,592.267\n"
        s += "599.189,586.015\n"
        self.assertEqual(ctl_points[2].to_s(),s)
    #end def testMakeCubicBezierCurve

    def testCreateCubicBezierCurveSetDict(self):
        curve_set_dict = createCubicBezierCurveSetDict("data/aaa.svg")
        self.assertListEqual(list(curve_set_dict.keys()), ["senga1", "senga2"])

        curve_set = curve_set_dict["senga1"]
        curves = curve_set.curves
        ctl_points = curves[0].control_points

        s = ""
        s += "624.369,665.275\n"
        s += "624.369,665.275\n"
        s += "615.909,650.653\n"
        s += "610.912,630.454\n"
        self.assertEqual(ctl_points[0].to_s(),s)

        s = ""
        s += "610.912,630.454\n"
        s += "605.916,610.254\n"
        s += "602.648,598.519\n"
        s += "602.648,598.519\n"
        self.assertEqual(ctl_points[1].to_s(),s)

        s = ""
        s += "602.648,598.519\n"
        s += "600.918,592.267\n"
        s += "600.918,592.267\n"
        s += "599.189,586.015\n"
        self.assertEqual(ctl_points[2].to_s(),s)

        ctl_points = curves[1].control_points
        s = ""
        s += "624.369,665.275\n"
        s += "624.369,665.275\n"
        s += "615.909,650.653\n"
        s += "610.912,630.454\n"
        self.assertEqual(ctl_points[0].to_s(),s)

        s = ""
        s += "610.912,630.454\n"
        s += "605.916,610.254\n"
        s += "602.648,598.519\n"
        s += "602.648,598.519\n"
        self.assertEqual(ctl_points[1].to_s(),s)

        s = ""
        s += "602.648,598.519\n"
        s += "600.918,592.267\n"
        s += "600.918,592.267\n"
        s += "599.189,586.015\n"
        self.assertEqual(ctl_points[2].to_s(),s)

    #end def testCreateCubicBezierCurveSetGroup

#end

if __name__ == '__main__':
    unittest.main()
#end
