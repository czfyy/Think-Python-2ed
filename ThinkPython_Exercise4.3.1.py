# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 13:33:04 2019

@author: czfyy
"""
import turtle

def square(t):

    for i in range(4):
        t.fd(100)
        t.lt(90)
bob = turtle.Turtle()
square(bob)         #参数为具体对象
print(type(bob)) 

'''
这么写也可以
def square(t):
    t = turtle.Turtle()
    for i in range(4):
        t.fd(100)
        t.lt(90)
square('bob')    #参数为对象名称，具体对象在函数中创建
'''