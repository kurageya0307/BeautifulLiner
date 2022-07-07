
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../logic'))
from read_cubic_bezier_curve_from_svg_file import *

import unittest

import pprint as pp
class TestCreateCubicBezierCurveSetGroup(unittest.TestCase):
    def testMakeCubicBezierCurve(self):
        d_str = 'M624.369 665.275C624.369 665.275 615.909 650.653 610.912 630.454C605.916 610.254 602.648 598.519 602.648 598.519L599.189 586.015'
        curve = makeCubicBezierCurve(d_str)

        s = ""
        s += "624.369,665.275\n"
        s += "624.369,665.275\n"
        s += "615.909,650.653\n"
        s += "610.912,630.454\n"
        self.assertEqual(curve[0].to_s(),s)

        s = ""
        s += "610.912,630.454\n"
        s += "605.916,610.254\n"
        s += "602.648,598.519\n"
        s += "602.648,598.519\n"
        self.assertEqual(curve[1].to_s(),s)

        s = ""
        s += "602.648,598.519\n"
        s += "600.342,590.183\n"
        s += "601.495,594.351\n"
        s += "599.189,586.015\n"
        self.assertEqual(curve[2].to_s(),s)
    #end def testMakeCubicBezierCurve

    def testReadCubicBezierCurveFromSvgFile(self):
        cubic_bezier_curve, space_index = readCubicBezierCurveFromSvgFile("data/aaa.svg")
        the_answer_layer_name = ("senga1", "senga2")
        the_answer_ctrl_points_str = \
        (   "624.369,665.275\n624.369,665.275\n615.909,650.653\n610.912,630.454\n",
            "610.912,630.454\n605.916,610.254\n602.648,598.519\n602.648,598.519\n",
            "602.648,598.519\n600.342,590.183\n601.495,594.351\n599.189,586.015\n",
            "625.695,667.640\n616.754,656.379\n600.038,581.965\n601.044,593.338\n",
            "601.044,593.338\n597.826,582.375\n614.663,657.151\n625.927,667.627\n",
            "625.927,667.627\n597.826,582.375\n614.663,657.151\n625.927,667.627\n" )
        
        i:int = 0
        j:int = 0
        for layer_name, curve_set_in_a_layer in cubic_bezier_curve:
            self.assertEqual(layer_name, the_answer_layer_name[i])
            for curve in curve_set_in_a_layer:
                for ctrl_p in curve:
                    self.assertEqual(ctrl_p.to_s(), the_answer_ctrl_points_str[j])
                    j += 1
                #end for
            #end for
            i += 1
        #end for

        #print( space_index )
    #end def testCreateCubicBezierCurveSetGroup

#end

if __name__ == '__main__':
    unittest.main()
#end
