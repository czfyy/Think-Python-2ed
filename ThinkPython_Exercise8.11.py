# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:41:39 2019

@author: czfyy
"""

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
  
    i = 0
    j = len(word2) - 1   #第一处错误
    
    while j >= 0:       #第二处错误
        if word1[i] != word2[j]:
            return False
        i = i + 1
        j = j - 1
        
    return True

print(is_reverse('kcam','mack'))