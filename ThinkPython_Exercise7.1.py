# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:14:35 2019

@author: czfyy
"""
'''
排版有问题！！！！！！！！！！！！！！
'''
import math

def mysqrt(a, x):
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < math.exp(-30):
            if x < math.exp(-10):   #x<exp(-10)时强制等于0
                x = 0
            return x
            break
        x = y

def text_square_root():
    for i in range(10):
        t = mysqrt(i, 2)
        mathsqrt = round(math.sqrt(i),10)
        diff = abs(t - math.sqrt(i))
        print(i, ' ',round(t,10), mathsqrt, round(diff,10))

text_square_root()