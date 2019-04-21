# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:19:49 2019

@author: czfyy
"""

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


if __name__ == '__main__':
    print(rotate_word('cheer', 7))
    print(rotate_word('melon', -10))
    print(rotate_word('sleep', 9))