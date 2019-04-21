# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:23:57 2019

@author: czfyy
"""

fin = open('word.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)