
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../controller'))
from create_cubic_bezier_curve_set import *

import unittest

import pprint as pp
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
        s += "600.342,590.183\n"
        s += "601.495,594.351\n"
        s += "599.189,586.015\n"
        self.assertEqual(ctl_points[2].to_s(),s)
    #end def testMakeCubicBezierCurve

    def testCreateCubicBezierCurveSet(self):
        cubic_bezier_curve_set = createCubicBezierCurveSet("data/aaa.svg")
        the_answer_group_id = ("senga1", "senga2")
        the_answer_ctrl_points_str = \
        (   "624.369,665.275\n624.369,665.275\n615.909,650.653\n610.912,630.454\n",
            "610.912,630.454\n605.916,610.254\n602.648,598.519\n602.648,598.519\n",
            "602.648,598.519\n600.342,590.183\n601.495,594.351\n599.189,586.015\n",
            "624.369,665.275\n624.369,665.275\n615.909,650.653\n610.912,630.454\n",
            "610.912,630.454\n605.916,610.254\n602.648,598.519\n602.648,598.519\n",
            "602.648,598.519\n600.918,592.267\n600.918,592.267\n599.189,586.015\n" )
        
        i:int = 0
        for group_id, curves in cubic_bezier_curve_set:
            j:int = 0
            for curve in curves:
                ctrl_p = curve.control_points
                for  ctrl_point in curve.control_points:
                    self.assertEqual(ctrl_point.to_s(), the_answer_ctrl_points_str[j])
                    j += 1
                #end for
            #end for
            self.assertEqual(group_id, the_answer_group_id[i])
            i += 1
        #end for
    #end def testCreateCubicBezierCurveSetGroup

#end

if __name__ == '__main__':
    unittest.main()
#end
