# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:43:11 2019

@author: czfyy
"""

import turtle
from ThinkPython_Exercise15 import rectangle

class circle:
    '''
    attributes: center,radius
    '''
    
class point:
    """Represents a point in 2-D space.

    attributes: x, y
    """
    
def draw_rect(t, rect):
    t.pu()
    t.goto(rect.corner.x, rect.corner.y)
    t.setheading(0)
    t.pd()
    for length in [rect.width, rect.height, rect.width, rect.height]:
        t.fd(length)
        t.rt(90)

if __name__ == '__main__':
    bob = turtle.Turtle()
    
    # draw the axes
    length = 400
    bob.fd(length)
    bob.bk(length)
    bob.lt(90)
    bob.fd(length)
    bob.bk(length)

    # draw a rectangle
    box = rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = point()
    box.corner.x = 50.0
    box.corner.y = 50.0

    draw_rect(bob, box)

    # wait for the user to close the window
    turtle.mainloop()