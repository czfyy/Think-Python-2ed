# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:15:44 2019

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

def check(num):
    if is_palindrome(str(num)[2:]) \
    and is_palindrome(str(num+1)[1:]) \
    and is_palindrome(str(num+2)[1:5]) \
    and is_palindrome(str(num+3)):
        return True
    else:
        return False

i = 100000
while i <= 999999:
    num = i
    if check(num):
        print(num)
    i += 1