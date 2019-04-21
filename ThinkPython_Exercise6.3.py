# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 15:08:55 2019

@author: czfyy
"""

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def palindrome(word):
    print(first(word))
    print(last(word))
    print(middle(word))
    
def is_palindrome(word):
    n = 0
    for i in range(len(word)) :
        if word[i] == word[(len(word)-1) - i]:
            n += 1
            print('程序检查 n =',n)
    if n == len(word):
        print('TRUE')
    else:
        print('FALSE')

t = input('input:')
if not isinstance(t, str):
    print('palidrome is only defined for string')
palindrome(t)
is_palindrome(t)

'''
答案解法
def is_palindrome(word):
    """Returns True if word is a palindrome."""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))
'''