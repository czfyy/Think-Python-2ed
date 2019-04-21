# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 21:16:53 2019

@author: czfyy
"""

def make_dict(t):
    d = {}
    for line in t:
        d[line.strip()] = line.strip()
    return d

def in_bisect(word_dict, word):
    for key in word_dict: #对于字典中的所有键
        if word_dict[key] == word:  #键值等于给定单词
            return True
    return False

word = open('word.txt')
word_dict = make_dict(word)
for word in ['el', 'eke', 'esssssss', 'aits']:
    print(word, 'in list', in_bisect(word_dict, word))