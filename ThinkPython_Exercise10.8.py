# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:51:40 2019

@author: czfyy
"""

import random

def has_duplicates(s):
    t = sorted(list(s))     #先对元素升序排列，若有重复字符，两元素必相邻
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            return True
    return False       

def random_bdays(n):
    t = []
    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)
    return t

def count_matches(num_students, num_simulations):
    count = 0
    for i in range(num_simulations):
        t = random_bdays(num_students)
        if has_duplicates(t):
            count += 1
    return count

def same_birthday(num_students):
    p_bar = 1
    i = 0
    while i < num_students:
        p_bar = p_bar * (1 - i/365)
        i += 1
    return round(1 - p_bar,5)

def main():
    num_students = int(input('students number: '))
    num_simulations = int(input('simulation number: '))
    count = count_matches(num_students, num_simulations)
    print()
    print('probability: ',same_birthday(num_students))
    print('After %d simulations' % num_simulations)
    print('with %d students' % num_students)
    print('there were %d simulations with at least one match' % count)

main()