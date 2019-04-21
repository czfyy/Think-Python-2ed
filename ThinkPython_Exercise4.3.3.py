# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:50:29 2019

@author: czfyy
"""

import turtle

def polygon(t,length,n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
bob = turtle.Turtle()
polygon(bob,length=100,n=6)
