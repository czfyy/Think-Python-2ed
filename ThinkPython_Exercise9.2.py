# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:34:23 2019

@author: czfyy
"""

def has_no_e(fin):
    total = 0
    count = 0
    for line in fin:
        total += 1
        word = line.strip()
        if word.find('e') == -1:
            print(word)
            count += 1
    print(round(count/total*100,2),'%')

        
fin = open('word.txt')
has_no_e(fin)

'''
        判断条件如下亦可以
def has_no_e(fin):
    total = 0
    count = 0
    for line in fin:
        total += 1
        word = line.strip()
        if 'e' not in word:
            print(word)
            count += 1
    print(round(count/total*100,2),'%')
'''