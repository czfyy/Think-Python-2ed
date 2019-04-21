# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:48:35 2019

@author: czfyy
"""

def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return gcd(b, a)
    else:
        r = a % b
        return gcd(b, r)

print(gcd(25,3))