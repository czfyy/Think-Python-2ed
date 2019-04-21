# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:48:53 2019

@author: czfyy
"""

fruit = 'banana'

'''
正序：（第一项是0）
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
    
倒序：（倒数最后一项用-1表示）
index = -1
while index >= 0 - len(fruit):
    letter = fruit[index]
    print(letter)
    index = index - 1
'''

for letter in fruit:
    print(letter)

#letter在此表示一个变量，fruit是str格式
#len(fruit) = 5 是一个具体数值
#for letter in range(fruit) 会报错TypeError: 'str' object cannot be interpreted as an integer
#因为range是用来产生一个数组，而fruit在这里是字符串
#若改为for letter in range(len(fruit))就可以产生一个0-5的数组了