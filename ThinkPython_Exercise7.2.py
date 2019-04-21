# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 15:18:29 2019

@author: czfyy
"""

def eval_loop():
    kk = ''
    while True:
        k = input('input: ')
        if k == 'done':
            print('result:',kk)
            print('Done!')
            break
        else:
            kk = kk + eval('k')
eval_loop()