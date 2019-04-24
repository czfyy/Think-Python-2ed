# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 22:59:25 2019

@author: czfyy
"""

def Ack(m, n):
    known = {}
    if m == 0:
        return n+1
    elif n == 0:
        return Ack(m-1, 1)
    
    if (m, n) in known: #(m,n)整体看作键，Ack(m,n)的结果看作键值
        return known[(m, n)]
    else:
        known[(m, n)] = Ack(m-1, Ack(m, n-1))
        print(known)
        return known[(m, n)]
        
t = Ack(3,4)
print(t)