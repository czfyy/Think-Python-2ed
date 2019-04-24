# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:41:20 2019

@author: czfyy
"""

def has_duplicates(s):
    d = dict()
    for letter in s:
        if letter in d:
            return True
        d[letter] = True #键值是啥不重要，只要将键添加进去就行
    return False

'''答案解法，set(s)中一样的元素只取一次，故长度小于等于len(s)
def has_duplicates(s):
    return len(set(s)) < len(s)
'''

t = 'asdfgh'
print(has_duplicates(t))