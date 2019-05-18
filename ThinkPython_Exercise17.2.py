# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:17:21 2019

@author: czfyy
"""

class Kangaroo:
    #如果形参为直接为pouch_contents = [] 那么这个contents的内容就成为公用的了，任何对象都可以对这个列表进行操作
    def __init__(self, name, pouch_contents=None):
        self.name = name
        if pouch_contents ==None:
            pouch_contents = []
        self.pouch_contents = pouch_contents
    
    def __str__(self):
        t = [self.name + ' has pouch contents:']
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)
    
    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')

kanga.put_in_pouch('wallet')
roo.put_in_pouch('car keys')
#kanga.put_in_pouch('car keys')

kanga.put_in_pouch(roo)

print(kanga)