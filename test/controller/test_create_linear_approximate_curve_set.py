
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../model'))
from point import Point

sys.path.append(os.path.join(os.path.dirname(__file__), '../../controller'))
from create_linear_approximate_curve_set import *
from create_cubic_bezier_curve_set import createCubicBezierCurveSet

import unittest

class TestApproximateCurveWithLineSegments(unittest.TestCase):
    def testGetEquallyDividedPointsBetween2Points(self):
        point_a = Point(0.0, 0.0)
        point_b = Point(10.0, 10.0)
        division_num = 10

        points = getEquallyDividedPointsBetween2Points(point_a, point_b, division_num)

        answer = []
        for i in range(division_num):
            answer.append( [float(i), float(i)] )
        #end for
        answer.append( [10.0, 10.0] )

        for i, point in enumerate(points):
            self.assertEqual(point.x, answer[i][0])
            self.assertEqual(point.y, answer[i][1])
            #print( "{}, {}, {}".format(i, point.x, point.y) )
        #end for

    #end def testGetEquallyDividedPointsBetween2Points

    def testGetInternalDivisionPoint(self):
        point_a = Point(1.0, 1.0)
        point_b = Point(10.0, 10.0)

        point = getInternalDivisionPoint(point_a, point_b, 1.0, 2.0)

        answer = [4.0, 4.0]
        self.assertEqual(point.x, answer[0])
        self.assertEqual(point.y, answer[1])
        #print( "{}, {}".format(point.x, point.y) )

    #end def testGetInternalDivisionPoint

    def testCreateLinearApproximateCurve(self):
        cubic_bezier_curve_set = createCubicBezierCurveSet("data/aaa.svg")
        linear_approximate_curve_set = createLinearApproximateCurve(cubic_bezier_curve_set, 1.0)

        answer = "<g id=\"senga1\">\n<path fill=\"none\" stroke-width=\"1.0\" stroke=\"#000000\" d=\"M 624.369 665.275 L 624.313 665.177 L 624.149 664.885 L 623.886 664.406 L 623.531 663.746 L 623.091 662.910 L 622.575 661.905 L 621.991 660.736 L 621.345 659.409 L 620.646 657.930 L 619.901 656.305 L 619.119 654.539 L 618.306 652.639 L 617.471 650.610 L 616.622 648.459 L 615.765 646.191 L 614.909 643.811 L 614.062 641.327 L 613.231 638.743 L 612.424 636.066 L 611.648 633.301 L 610.912 630.454 L 610.210 627.626 L 609.533 624.916 L 608.881 622.325 L 608.256 619.855 L 607.658 617.509 L 607.089 615.289 L 606.549 613.197 L 606.040 611.235 L 605.562 609.404 L 605.117 607.708 L 604.705 606.149 L 604.328 604.728 L 603.986 603.447 L 603.680 602.310 L 603.412 601.317 L 603.183 600.471 L 602.993 599.774 L 602.844 599.228 L 602.736 598.835 L 602.670 598.598 L 602.648 598.519 L 601.998 596.169 L 601.547 594.540 L 601.239 593.425 L 601.016 592.619 L 600.821 591.915 L 600.598 591.109 L 600.290 589.994 L 599.839 588.365 \"/>\n<path fill=\"none\" stroke-width=\"1.0\" stroke=\"#000000\" d=\"M 624.369 665.275 L 624.313 665.177 L 624.149 664.885 L 623.886 664.406 L 623.531 663.746 L 623.091 662.910 L 622.575 661.905 L 621.991 660.736 L 621.345 659.409 L 620.646 657.930 L 619.901 656.305 L 619.119 654.539 L 618.306 652.639 L 617.471 650.610 L 616.622 648.459 L 615.765 646.191 L 614.909 643.811 L 614.062 641.327 L 613.231 638.743 L 612.424 636.066 L 611.648 633.301 L 610.912 630.454 L 610.210 627.626 L 609.533 624.916 L 608.881 622.325 L 608.256 619.855 L 607.658 617.509 L 607.089 615.289 L 606.549 613.197 L 606.040 611.235 L 605.562 609.404 L 605.117 607.708 L 604.705 606.149 L 604.328 604.728 L 603.986 603.447 L 603.680 602.310 L 603.412 601.317 L 603.183 600.471 L 602.993 599.774 L 602.844 599.228 L 602.736 598.835 L 602.670 598.598 L 602.648 598.519 L 602.003 596.186 L 601.508 594.400 L 601.105 592.941 L 600.732 591.593 L 600.329 590.134 L 599.834 588.348 \"/>\n</g><g id=\"senga2\">\n<path fill=\"none\" stroke-width=\"1.0\" stroke=\"#000000\" d=\"M 624.369 665.275 L 624.313 665.177 L 624.149 664.885 L 623.886 664.406 L 623.531 663.746 L 623.091 662.910 L 622.575 661.905 L 621.991 660.736 L 621.345 659.409 L 620.646 657.930 L 619.901 656.305 L 619.119 654.539 L 618.306 652.639 L 617.471 650.610 L 616.622 648.459 L 615.765 646.191 L 614.909 643.811 L 614.062 641.327 L 613.231 638.743 L 612.424 636.066 L 611.648 633.301 L 610.912 630.454 L 610.210 627.626 L 609.533 624.916 L 608.881 622.325 L 608.256 619.855 L 607.658 617.509 L 607.089 615.289 L 606.549 613.197 L 606.040 611.235 L 605.562 609.404 L 605.117 607.708 L 604.705 606.149 L 604.328 604.728 L 603.986 603.447 L 603.680 602.310 L 603.412 601.317 L 603.183 600.471 L 602.993 599.774 L 602.844 599.228 L 602.736 598.835 L 602.670 598.598 L 602.648 598.519 L 601.998 596.169 L 601.547 594.540 L 601.239 593.425 L 601.016 592.619 L 600.821 591.915 L 600.598 591.109 L 600.290 589.994 L 599.839 588.365 \"/>\n<path fill=\"none\" stroke-width=\"1.0\" stroke=\"#000000\" d=\"M 624.369 665.275 L 624.313 665.177 L 624.149 664.885 L 623.886 664.406 L 623.531 663.746 L 623.091 662.910 L 622.575 661.905 L 621.991 660.736 L 621.345 659.409 L 620.646 657.930 L 619.901 656.305 L 619.119 654.539 L 618.306 652.639 L 617.471 650.610 L 616.622 648.459 L 615.765 646.191 L 614.909 643.811 L 614.062 641.327 L 613.231 638.743 L 612.424 636.066 L 611.648 633.301 L 610.912 630.454 L 610.210 627.626 L 609.533 624.916 L 608.881 622.325 L 608.256 619.855 L 607.658 617.509 L 607.089 615.289 L 606.549 613.197 L 606.040 611.235 L 605.562 609.404 L 605.117 607.708 L 604.705 606.149 L 604.328 604.728 L 603.986 603.447 L 603.680 602.310 L 603.412 601.317 L 603.183 600.471 L 602.993 599.774 L 602.844 599.228 L 602.736 598.835 L 602.670 598.598 L 602.648 598.519 L 602.003 596.186 L 601.508 594.400 L 601.105 592.941 L 600.732 591.593 L 600.329 590.134 L 599.834 588.348 \"/>\n</g>"
        self.assertEqual( linear_approximate_curve_set.to_svg_str(), answer)
    #end deff

#end

#end class

if __name__ == '__main__':
    unittest.main()
#end
