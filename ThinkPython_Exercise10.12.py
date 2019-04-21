# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:19:10 2019

@author: czfyy
"""

def twowayinterlock(word):
    a = []
    b = []
    joinedword = []
    i = 0
    while i <= len(word)-1:
        a += [word[i]]
        if i < len(word)-1:
            b += [word[i+1]]
        elif i == len(word)-1:
            pass
        i += 2
    word1 = ''.join(a)
    word2 = ''.join(b)
    joinedword.append(word1)
    joinedword.append(word2)
    return joinedword

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

word_list = word_list()
for word in word_list:
    joinedword = twowayinterlock(word)
    if in_bisect(word_list, joinedword[0]) \
    and in_bisect(word_list, joinedword[1]):
        print(word,joinedword[0],joinedword[1])

'''参考答案，直接用切片更方便
def interlock(word_list, word):
    """Checks whether a word contains two interleaved words.

    word_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
        

def interlock_general(word_list, word, n=3):
    """Checks whether a word contains n interleaved words.

    word_list: list of strings
    word: string
    n: number of interleaved words
    """
    for i in range(n):
        inter = word[i::n]
        if not in_bisect(word_list, inter):
            return False
    return True
'''