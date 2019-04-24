# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:48:16 2019

@author: czfyy
"""

def histogram(s): #统计字母出现次数
    d = dict()
    for letter in s:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
    return d

def print_hist(h):  #按ASCII码顺序打印键与键值
    h_list = h.keys()
    for letter in sorted(h_list):
        print(letter, h[letter])

def reverse_lookup(d, v):  #逆向查找（通过键值找键）
    for key in d:
        if d[key] == v:
            return key
    raise ValueError('value does not appear in the dictionary')


def invert_dict(d): #以频次为键，字母列表为键值
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key] #inverse虽然为字典，但对于具体键inverse[val]为列表，例如inverse[2],inverse[1]
        else:                   #故inverse[val]的赋值应为[key],即先生成一个包含元素key的新列表，再往里面填元素
            inverse[val].append(key)
    return inverse

h = histogram('asdfgasdfghjklzzz')
print_hist(h)
k = invert_dict(h)
print_hist(k)