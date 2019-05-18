# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:41:44 2019

@author: czfyy
"""

def sed(pattern, replace, source, dest):
    fin = open(source, 'r')
    fout = open(dest, 'w')
    for line in fin:
        line = line.replace(pattern, replace)
        fout.write(line)
    
    fin.close()
    fout.close()

def main():
    pattern = 'pattern'
    replace = 'replace'
    source = ''
    dest = source + '.replaced'
    sed(pattern, replace, source, dest)

if __name__ == '__main__':
    main()