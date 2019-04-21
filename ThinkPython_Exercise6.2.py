# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:47:44 2019

@author: czfyy
"""

def Ack(m, n):
    if not isinstance(m, int):
        print('Factorial is only defined for integers.')
    elif m < 0 or n <0:
        print('Ack is not defined for negative integers')
    elif m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return(Ack(m - 1, 1))
    elif m > 0 and n > 0:
        return(Ack(m - 1, Ack(m, n - 1)))
        
t = Ack(3,4)
print(t)