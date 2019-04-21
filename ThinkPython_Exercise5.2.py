# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 14:08:19 2019

@author: czfyy
"""

def check_fermat(a, b, c, n):
    A = a**n
    B = b**n
    C = c**n
    if (A + B) == C:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')

def input_para():
    a = int(input('input a: '))
    b = int(input('input b: '))
    c = int(input('input c: '))
    n = int(input('input n: '))
    if (a and b and c) <= 0:
        print('abc应为正整数')
        input_para()
    elif n <= 2 :
        print('n应大于2')
        input_para()
    else:
        check_fermat(a, b, c, n)

input_para()