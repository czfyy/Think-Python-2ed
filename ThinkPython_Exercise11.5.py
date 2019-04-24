# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:51:06 2019

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

def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter
    c = ord(letter) - start
    i = (c + n) % 26 + start  #除以26取余是为了保证偏移量还在26个字母范围内
    return chr(i)


def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:                   #res从空字符串开始
        res += rotate_letter(letter, n)   #对每个字母逐项移位并将其连接到一起
    return res

def rotate_pairs(word, word_dict):
    for i in range(1,14): #将单词字母移位1到14位，判断移位后的新单词是否在表中
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print(word, i, rotated)

word = open('word.txt')
word_dict = make_dict(word)
for word in word_dict:
    rotate_pairs(word, word_dict)