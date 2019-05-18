# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:49:23 2019

@author: czfyy
"""

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def choose_from_hist(t):
    sum = 0
    p = dict()
    hist = histogram(t)
    '''用循环
    for key in hist:
        sum += hist[key]
        
    用values也可以
    for value in hist.values():
        sum += value
    '''
    for key in hist:
        p[key] = hist[key] / sum
        
    return p

t = 'aaaab'
print(choose_from_hist(t))