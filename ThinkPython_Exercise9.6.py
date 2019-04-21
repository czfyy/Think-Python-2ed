# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:01:59 2019

@author: czfyy
"""

def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])

word = input('word:')
if is_abecedarian(word):
    print('True')
else:
    print('False')      
