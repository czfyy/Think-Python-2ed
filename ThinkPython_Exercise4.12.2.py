# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:32:42 2019

@author: czfyy
"""
import math
import turtle

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle/360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def petal(t, r, angle):
    for i in range(2):
        arc(t ,r ,angle)
        t.lt(180-angle)

def flower(t, n, r, angle): #t名称，n瓣数，r花瓣弧所对应的半径，angle一瓣的角度
    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n)     #petal中每画完一段弧都会旋转180-angle，所以这里需要再旋转360/n度，而不是转180度
        print(i,'+',360/n)

def move(t, length):   #调整图像位置
    t.pu()
    t.fd(length)
    t.pd()

bob = turtle.Turtle()

move(bob, -100)
flower(bob,7,150,80) #角度也可以用360/n计算，但这样就画不了第二个图了
'''
move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)
'''