# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:40:15 2019

@author: czfyy
"""
#二叉树？？

import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 45
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

bob = turtle.Turtle()
draw(bob, 30, 4)