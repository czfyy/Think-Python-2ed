# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:00:16 2019

@author: czfyy
"""

import turtle
import math

def polygon(t,length,n):
    t = turtle.Turtle()
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
def circle(t,r):
    c = 2 * math.pi * r
    n = int(c/3) + 1 #线段数量为周长的1/3，+1是为了避免n=0
    length = c / n
    polygon(t,length,n)

circle('bob',100)