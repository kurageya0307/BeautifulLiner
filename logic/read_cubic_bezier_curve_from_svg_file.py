
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

from svg_data import SvgData
from point import Point
from cubic_bezier_control_point import CubicBezierControlPoint
from cubic_bezier_curve import CubicBezierCurve
from cubic_bezier_curve_set import CubicBezierCurveSet

from part_of_curve import PartOfCurve
from curve import Curve
from curve_set_in_a_layer import CurveSetInALayer
from all_curve_set import AllCurveSet

import pprint as pp
import re

# IN  nodeValue of d in path of svg as string
# OUT CubicBezierCurve
def makeCubicBezierCurve(d_str):
    curve = Curve()

    point_strs = re.split("[C|L|M|Z]", d_str)
    point_strs.pop(0)


    # exception handling for 1st point
    items = re.split( "\s+", point_strs[0].strip() )
    last_point = Point( float(items[0]), float(items[1]) )
    point_strs.pop(0)

    for point_str in point_strs:
        items = re.split( "\s+", point_str.strip() )
        if len(items)==2:
            p3 = Point( float(items[0]), float(items[1]) )
            x1, y1, x2, y2 = 0.0, 0.0, 0.0, 0.0
            if (last_point.x < p3.x):
                x1 = (last_point.x*2.0 + p3.x*1.0)/3.0
                x2 = (last_point.x*1.0 + p3.x*2.0)/3.0
            else:
                x1 = (last_point.x*1.0 + p3.x*2.0)/3.0
                x2 = (last_point.x*2.0 + p3.x*1.0)/3.0
            #end if
            if (last_point.y < p3.y):
                y1 = (last_point.y*2.0 + p3.y*1.0)/3.0
                y2 = (last_point.y*1.0 + p3.y*2.0)/3.0
            else:
                y1 = (last_point.y*1.0 + p3.y*2.0)/3.0
                y2 = (last_point.y*2.0 + p3.y*1.0)/3.0
            #end if
            p1 = Point(x1, y1)
            p2 = Point(x2, y2)
        elif len(items)==6:
            p1 = Point( float(items[0]), float(items[1]) )
            p2 = Point( float(items[2]), float(items[3]) )
            p3 = Point( float(items[4]), float(items[5]) )
        #end if
        part = PartOfCurve()
        part.set_control_point( CubicBezierControlPoint(last_point, p1, p2, p3) )
        curve.append(part)
        last_point = p3
    #end for

    return curve
#end def

def makeCubicBezierCurveSet(paths):
    curve_set = CurveSetInALayer()
    for path in paths:
        curve_set.append(  makeCubicBezierCurve( path.getAttributeNode('d').nodeValue )  )
    #end for
    return curve_set
#end

# IN  file_name as string
# OUT AllCurveSet
def readCubicBezierCurveFromSvgFile(file_name):
    cubic_bezier_curve = AllCurveSet()
    
    svg = SvgData(file_name)
    for group_paths_set in svg.get_group_paths_tuple():
        group = group_paths_set[0]
        paths = group_paths_set[1]
        layer_name = group.getAttributeNode('id').nodeValue
        cubic_bezier_curve.append(layer_name, makeCubicBezierCurveSet(paths) )
    #end for group_paths_set

    return cubic_bezier_curve
#end def