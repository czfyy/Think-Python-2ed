# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:47:19 2019

@author: czfyy
"""

import math
import copy
from ThinkPython_Exercise15 import rectangle

class circle:
    '''
    attributes: center,radius
    '''
    
class point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

def distance_between_point(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx*dx + dy*dy)
    return dist

def point_in_circle(circle, point):
    d = distance_between_point(circle.center, point)
    if d <= circle.radius:
        return True
    else:
        return False

def rect_in_circle(circle, rect):
    p = copy.copy(rect.corner)
    if not point_in_circle(circle, p):
        return False
    
    p.x += rect.width
    if not point_in_circle(circle, p):
        return False
    
    p.y += rect.height
    if not point_in_circle(circle, p):
        return False
    
    p.x -=rect.width
    if not point_in_circle(circle, p):
        return False
    return True

def rect_circle_overlap(circle, rect):
    p = copy.copy(rect.corner)
    if not point_in_circle(circle, p):
        return True
    
    p.x += rect.width
    if not point_in_circle(circle, p):
        return True
    
    p.y += rect.height
    if not point_in_circle(circle, p):
        return True
    
    p.x -=rect.width
    if not point_in_circle(circle, p):
        return True
    return False

def main():
    box = rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    print(box.corner.x)
    print(box.corner.y)

    cir = circle()
    cir.center = point()
    cir.center.x = 150.0
    cir.center.y = 100.0
    cir.radius = 75.0

    print(cir.center.x)
    print(cir.center.y)
    print(cir.radius)

    print(point_in_circle(cir, box.corner))
    print(rect_in_circle(cir, box))
    print(rect_circle_overlap(cir, box))


if __name__ == '__main__':
    main()
