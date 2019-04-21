# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:29:15 2019

@author: czfyy
"""

import time

def word_list1(fin):
    word = []
    for line in fin:
        x = line.strip()
        word += [x]
    return word

def word_list2(fin):
    word = []
    for line in fin:
        word.append(line.strip())
    return word

fin = open('word.txt')

start_time = time.time()
word2 = word_list2(fin)
elapsed_time = time.time() - start_time
print(round(elapsed_time, 6), 'seconds')
print(len(word2))
