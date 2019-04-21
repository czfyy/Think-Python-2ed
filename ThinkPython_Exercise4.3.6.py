# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:27:39 2019

@author: czfyy
"""

#通过接口重写circle,polygon
import math
import turtle 

def polyline(t, n, length, angle):
    t = turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)
    
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)
circle('a',200)
arc('b',200,90)
polygon('c',8,50)
