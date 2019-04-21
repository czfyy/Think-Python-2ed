# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:18:37 2019

@author: czfyy
"""
'''
n>=0时求和
'''
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 0)
