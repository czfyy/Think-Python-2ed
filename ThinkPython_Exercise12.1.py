# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:00:19 2019

@author: czfyy
"""

def frequent(s):
    h = histogram(s)
    
    t = []
    for x, freq in h.items():
        t.append((freq, x))
        
    t.sort(reverse = True)
    
    res = []
    for freq, x in t:
        res.append(x)
        
    return res

def histogram(s):
    hist = {}
    for x in s:
        hist[x] = hist.get(x, 0) + 1
    return hist

def read_file(filename):
    return open(filename).read()

string = read_file('theater.txt')
letter_seq = frequent(string)
print(letter_seq)