# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:56:34 2019

@author: czfyy
"""

#task1 version1
print('task1 version1:')
print('+ - - - + - - - +')
print('|       |       |')
print('|       |       |')
print('|       |       |')
print('|       |       |')
print('+ - - - + - - - +')
print('|       |       |')
print('|       |       |')
print('|       |       |')
print('|       |       |')
print('+ - - - + - - - +')
print()

#task1 version2
def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)
    
def print_beam():
    print('+ - - - -',end=' ') #+ - - - -为一组
def print_post():
    print('|        ',end=' ') #|        为一组 

def print_beams():  #两组+-外加一个+号组成一行边界 “+ - - - - + - - - - +”
    do_twice(print_beam) 
    print('+')
def print_posts():  #两组| 外加一个|号组成方框内部 “|         |         |”
    do_twice(print_post)
    print('|')

def print_row(): #一个外边界，四个内边界
    print_beams()
    do_four(print_posts)
    
def print_2grid():
    do_twice(print_row) #print_row中组成的单元×2
    print_beams()       #方框最后一行 “+ - - - - + - - - - +”
print('task1 version2:')
print_2grid()
print()

#task2 version1
def print_4beams():
    do_four(print_beam)
    print('+')
def print_4posts():
    do_four(print_post)
    print('|')

def print_4row():
    print_4beams()
    do_four(print_4posts)

def print_4grid():
    do_four(print_4row)
    print_4beams()
print('task2 version1:')
print_4grid()
print()

#task2 version2
def one_four_one(f,g,h):
    f()
    do_four(g)
    h()
def print_plus():
    print('+',end=' ')
def print_dash():
    print('-',end=' ')
def print_bar():
    print('|',end=' ')
def print_space():
    print(' ',end=' ')
def print_end():
    print()
def nothing():
    'do nothing'
#画1*1小方块边界
def print1beam():
    one_four_one(nothing, print_dash, print_plus)
def print1post():
    one_four_one(nothing, print_space, print_bar)
#画4*4大方块边界
def print4beams():  #大方块外边界
    one_four_one(print_plus, print1beam, print_end)
def print4posts():  #大方块内边界
    one_four_one(print_bar, print1post, print_end)
#组成方块
def print_4row2():
    one_four_one(print4beams, print4posts, nothing)
def print_4grid2():
    one_four_one(nothing, print_4row2, print4beams)
print('task2 version2:')
print_4grid2()