# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:27:17 2019

@author: czfyy
"""

#task 1
def do_twice(f):
    f()
    f()

def print_spam():
    print('task1: spam')

do_twice(print_spam) #打印两个spam
print('')

#task 2
def do_twice1(f,x):
    f(x)
    f(x) 
def print_spam(k):
    print('task2: ',k)

do_twice1(print_spam,233) #打印两个233
print('')

#task 3/4 正确答案
def print_twice(arg):
    print('task3/4: ',arg)     
    print('task3/4: ',arg)

do_twice1(print_twice,'spam') #打印四个spam
print('')

'''
#task 3/4 错误调用示范
1.直接调用print_twice(233)可以打印两次，
但如果通过do_twice2函数间接调用print_twice函数，
需要将对象和参数分别传递，为什么不能写成以下形式？？
其中第二个参数233为什么用不到？？
do_twice2(print_twice('spam'),233)

2.改成以下形式也不行，只能打印两个233，实际应该是四个
且仍显示'NoneType' object is not callable
def do_twice3(f):
    f()
    f()
do_twice3(print_twice(233))

'''

#task 5
def do_four(f,x):
    do_twice1(f,x)
    do_twice1(f,x)

def print_spam1(arg):
    print('task5: ',arg)     
    
do_four(print_spam1,'spam')