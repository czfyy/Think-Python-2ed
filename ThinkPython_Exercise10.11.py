# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:49:01 2019

@author: czfyy
"""

def in_bisect(word_list, word):
    if len(word_list) == 0:
        return False
    
    i = len(word_list) // 2
    if word_list[i] == word:
        return True
    
    if word_list[i] > word:
        return in_bisect(word_list[:i], word)
    else:
        return in_bisect(word_list[i+1:], word)

def word_list():
    word_list = []
    fin = open('word.txt')
    for line in fin:
        word_list += [line.strip()]
        #word_list.append(line.strip())
    return word_list

def reverse_pair(word_list, word):
    reversed_word = word[::-1]
    return in_bisect(word_list, reversed_word)

word_list = word_list()
for word in word_list:
    if reverse_pair(word_list, word):
        print(word, word[::-1])