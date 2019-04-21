# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:54:09 2019

@author: czfyy
"""
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result
    
def estimate_pi():
    k = 0
    t = 0
    factor = 2 * math.sqrt(2) / 9801
    
    while True:
        num = factorial(4*k) * (1103+26390*k)
        den = factorial(k)**4 * 396**(4*k)
        term = factor * num / den
        t = t + term
        if abs(term) < math.exp(-15):
            break
        k += 1
        
    return 1/t

print(estimate_pi())