# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:51:34 2019

@author: czfyy
"""

def is_palindrome(word):
    i = 0
    j = len(word)-1
    while i<j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1
    return True

def check(fin):
    for line in fin:
        word = line.strip()
        if is_palindrome(word):
            print(word)

fin = open('word.txt')
check(fin)                