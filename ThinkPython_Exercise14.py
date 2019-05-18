# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:16:44 2019

@author: czfyy
"""
import os

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

def walks(dirname):
    
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

if __name__ == '__main__':
    print(linecount('ThinkPython_Exercise14.py'))