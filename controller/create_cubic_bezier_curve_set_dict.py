
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))

from svg_data import SvgData
from point import Point
from cubic_bezier_control_point import CubicBezierControlPoint
from cubic_bezier_curve import CubicBezierCurve
from cubic_bezier_curve_set import CubicBezierCurveSet

import pprint as pp
import re

# IN  nodeValue of d in path of svg as string
# OUT CubicBezierCurve
def makeCubicBezierCurve(d_str):
    cubic_bezier_curve = CubicBezierCurve()

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
        ctl_p = CubicBezierControlPoint(last_point, p1, p2, p3)
        cubic_bezier_curve.append(ctl_p)
        last_point = p3
    #end for

    return cubic_bezier_curve
#end def

# IN  file_name as string
# OUT {"group_id": CubicBezierCurveSet, "group_id":CubicBezierCurveSet, ...} as dict
#      group_id is name of layer in Vectornator or Inkscape
def createCubicBezierCurveSetDict(file_name):
    cubic_bezier_curve_set_dict = {}
    
    svg = SvgData(file_name)
    for group_paths_set in svg.get_group_paths_tuple():
        group = group_paths_set[0]
        paths = group_paths_set[1]
        group_id = group.getAttributeNode('id').nodeValue
        cubic_bezier_curve_set_dict[group_id] = CubicBezierCurveSet()
        for path in paths:
            cubic_bezier_curve_set_dict[group_id].append( makeCubicBezierCurve(path.getAttributeNode('d').nodeValue) )
        #end for path
    #end for group_paths_set

    return cubic_bezier_curve_set_dict
#end def
