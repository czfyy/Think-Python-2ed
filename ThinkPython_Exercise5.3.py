# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:03:22 2019

@author: czfyy
"""
#判断三次太麻烦，如何简化？？？
def is_trangle(a, b, c):
    if a + b <= c:
        print('no')
    elif a + c <= b:
        print('no')
    elif b + c <= a:
        print('no')
    else:
        print('yes')

def input_para():
    a = int(input('input a: '))
    b = int(input('input b: '))
    c = int(input('input c: '))
    if (a and b and c) <= 0:
        print('abc应为正整数')
        input_para()
    else:
        is_trangle(a, b, c)

input_para()