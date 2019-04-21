# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 09:26:07 2019

@author: czfyy
"""

#没看懂。。。

import turtle

def draw_spiral(t, n, length=3, a=0.1, b=0.0002):
    """Draws an Archimedian spiral starting at the origin.

    Args:
      n: how many line segments to draw
      length: how long each segment is
      a: how loose the initial spiral starts out (larger is looser)
      b: how loosly coiled the spiral is (larger is looser)

    http://en.wikipedia.org/wiki/Spiral
    """
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)  #???干啥呢这是

        t.lt(dtheta)
        theta += dtheta

# create the world and bob
bob = turtle.Turtle()
draw_spiral(bob, n=1000)
