# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:29:20 2019

@author: czfyy
"""
import math
V = (4/3)*math.pi*(5**3)
print('Exercise2.1: the volume of the sphere with radius 5 is',V)
print(' ')

price = (24.95*0.6 + 3)*60 - 59*(3-0.75) 
#邮费都按三块钱计算，再从总数里减去多出来的邮费
print('Exercise2.2: the total wholesale cost for 60 copies is',price)
print(' ')

minutes_total = (8+7*3+8+(15+12*3+15)/60)*2 #来回时间*2
hour = int(minutes_total//60)
minute = int((minutes_total % 60))
#不考虑秒
if 52 + minute >= 60:
    hour = hour + 1 + 8
    minute = 52 + minute - 60 

print(hour,minute)
print('Exercise2.3: you will get home at ',hour,':',minute,'for breakfast')