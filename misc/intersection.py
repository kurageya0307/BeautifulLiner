from sympy.geometry import *
import itertools
import matplotlib.pyplot as plt

def showPoints(target_points, other_points_sets):
    ##show points
    plt.figure()
    for i, p in enumerate(target_points):
        plt.plot(p.x, p.y,marker='.')
    for ii, pp in enumerate(other_points_sets):
        for i, p in enumerate(pp):
            plt.plot(p.x, p.y,marker='.')
    plt.show()
#end

def showRemovedPoints(removed_points):
    ##show points
    plt.figure()
    for i, p in enumerate(removed_points):
        plt.plot(p.x, p.y,marker='.')
    plt.show()
#end

def getRemoveStartingIndexAndPoint(tip_or_terminal, other_points_sets):
    for target_point_index in range( len(tip_or_terminal)-1 ):
        target_segment = Segment( tip_or_terminal[target_point_index], tip_or_terminal[target_point_index+1] )
        for other_points in other_points_sets:
            for other_point_index in range( len(other_points)-1 ):
                other_segment = Segment( other_points[other_point_index], other_points[other_point_index+1] )
                intersect = target_segment.intersection(other_segment)
                if intersect != []:
                    return target_point_index, intersect[0]
                #end if
            #end
        #end
    #end
    return None, None
#end

def getRemovedPoints(target_points, other_points_sets, ratio):
    int_ratio = int( len(target_points)*ratio )
    tip_targets = target_points[0:int_ratio]
    terminal_targets = target_points[ len(target_points)-int_ratio:len(target_points) ] 
    terminal_targets.reverse()
    #print(tip_targets)
    #print(terminal_targets)

    tip_index, tip_point = getRemoveStartingIndexAndPoint(tip_targets, other_points_sets)
    #print(tip_index)
    terminal_index, terminal_point = getRemoveStartingIndexAndPoint(terminal_targets, other_points_sets)
    #print(terminal_index)

    index_range_after_removed = [ 0, len(target_points) ]
    if tip_index is not None:
        index_range_after_removed[0] = tip_index + 1
    #end if
    if terminal_index is not None:
        index_range_after_removed[1] = len(target_points) - terminal_index - 1
    #end if


    removed_points = []
    if tip_point is not None:
        removed_points.append(tip_point)
    #end if
    for i in range( index_range_after_removed[0], index_range_after_removed[1] ):
        removed_points.append(target_points[i])
    #end for
    if terminal_point is not None:
        removed_points.append(terminal_point)
    #end if

    return removed_points


#end

def main():
    POINT_NUM = 20

    target_points = []
    for i in range(POINT_NUM):
        target_points.append( Point(i, i, evaluate=False) )
    #end for

    other_points_sets = []
    for i in range(1, POINT_NUM):
        tmp_points = []
        tmp_points.append( Point(0, i + 0.1, evaluate=False) )
        tmp_points.append( Point(i + 0.1, 0, evaluate=False) )
        other_points_sets.append( tmp_points )
    #end for

    #showPoints(target_points, other_points_sets)

    removed_points = getRemovedPoints(target_points, other_points_sets, 0.3)

    showRemovedPoints(removed_points)




#end main

main()