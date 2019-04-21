# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 19:33:01 2019

@author: czfyy
"""

def avoids(fin, letter):
    for line in fin:
        word = line.strip()
        if letter not in word:
            print(word)

fin = open('word.txt')
letter = input('enter a string of forbidden letters: ')
avoids(fin, letter)