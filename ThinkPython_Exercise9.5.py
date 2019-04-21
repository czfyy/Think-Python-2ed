# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 20:08:25 2019

@author: czfyy
"""

#判断word中每一个字母是否在给定string中，若存在，则删除string中的该字母，直到string长度为0
def use_all(word, mystring):
    for letter in word:
        if letter in mystring:
            i = mystring.find(letter)
            mystring = mystring[:i] + mystring[i+1:]
    if len(mystring) == 0:
        return True
    else:
        return False
            
word = input('word:')
mystring = input('string: ')
if use_all(word, mystring):
    print('use all')
else:
    print('not use all')    
