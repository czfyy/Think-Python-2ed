# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:37:56 2019

@author: czfyy
"""

def nest_sum(t):
    k = 0
    for e in t:
        k += sum(e)
    return k

def cumsum(t):
    k = 0
    res = []
    for i in t:
        k += i
        res.append(k) #append()函数无返回值
    return res

def middle(t):
    res = t[1:-1]
    return res

def chop(t):
    del t[0]
    del t[-1]

def is_sorted(t):
    if sorted(t) == t: #不能用t.sort() == t
        return True    #因为t.sort()结果是永久的,而sorted(t)结果是临时的
    else:               #若用sort(),则t.sort()和t分别指向两个对象，必定不等于（identical）t
        return False

def is_anagram(word1, word2):
    if sorted(word1) == sorted(word2):
        return True
    
def has_duplicates(s):
    t = sorted(list(s))     #先对元素升序排列，若有重复字符，两元素必相邻
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False           #若整个循环都没返回True,则说明没有相邻的字符相同，即没用重复项

'''另解
def has_duplicates(s):
    for i in range(len(s)): #对于s中的某一元素，若该元素在不包含该项的子列中有重复，则返回true
        t = list(s)
        k = t[i]
        t.remove(t[i])
        print(t)
        if k in t:
            return True
    return False
'''

t = [1, 2, 2, 4]
print(t)
print(has_duplicates(t))
print(has_duplicates('cba'))
print(has_duplicates('abba'))