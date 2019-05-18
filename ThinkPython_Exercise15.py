# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:28:39 2019

@author: czfyy
"""

import copy
import math

class point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))

class rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

def distance_between_point(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    dist = math.sqrt(dx*dx + dy*dy)
    return dist

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle_deepcopy(rect, dx, dy):
    new_rect = copy.deepcopy(rect)
    move_rectangle(new_rect, dx, dy)
    return new_rect