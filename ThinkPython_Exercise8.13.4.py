# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 13:42:38 2019

@author: czfyy
"""
#islower:如果字符串中包含至少一个区分大小写的字符，并且所有这些
#(区分大小写的)字符都是小写，则返回 True，否则返回 False

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
def any_lowercase2(s):  #字符串c是区分大小写的
    for c in s:         #故‘c’.islower必定恒是true
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
        
def any_lowercase3(s):
    for c in s:
        flag = c.islower()
        return flag
    
def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        return flag
    
def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
        return True
kkk = '555$%^@'
mmm = 'ssr555*&&'
print('1',any_lowercase1(kkk),any_lowercase1(mmm))
print('2',any_lowercase2(kkk),any_lowercase2(mmm))
print('3',any_lowercase3(kkk),any_lowercase3(mmm))
print('4',any_lowercase4(kkk),any_lowercase4(mmm))
print('5',any_lowercase5(kkk),any_lowercase5(mmm))
