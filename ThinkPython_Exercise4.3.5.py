# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 17:04:13 2019

@author: czfyy
"""
import turtle
import math

def arc(t, r, angle):
    t = turtle.Turtle()
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)
arc('g',300,90)
