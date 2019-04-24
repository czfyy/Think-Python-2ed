# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:58:12 2019

@author: czfyy
"""

def make_word_dict():
    d = {'a':'a', 'i':'i', '':''}
    fin = open('word.txt')
    for line in fin:
        d[line.strip().lower()] = line.strip().lower()
    return d

memo = {'':''}

def is_reducible(word, word_dict):
    if word in memo:
        return memo[word]
    
    res = []
    for child in children(word, word_dict):
        if is_reducible(child, word_dict):
            res.append(word)
    
    memo[word] = res
    return res

def children(word, word_dict):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)
    return res

def all_reducible(word_dict):
    res = []
    for word in word_dict:
        t = is_reducible(word, word_dict)
        if t != []:
            res.append(word)
    return res

#下面的没看懂。。。。。。。。。。。。。。。。
def print_trail(word):
    """Prints the sequence of words that reduces this word to the empty string.

    If there is more than one choice, it chooses the first.

    word: string
    """
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word)
    print_trail(t[0])

def print_longest_words(word_dict):
    """Finds the longest reducible words and prints them.

    word_dict: dictionary of valid words
    """
    words = all_reducible(word_dict)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for _, word in t[0:5]:
        print_trail(word)
        print('\n')


if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_words(word_dict)
