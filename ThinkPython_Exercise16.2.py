# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:37:24 2019

@author: czfyy
"""

from datetime import datetime

def datetoday():
    today = datetime.today()
    print(today.weekday())
    print(today.strftime('%A'))

def age_and_birthday(birthday):
    today = datetime.today()
    next_birthday = datetime(today.year, birthday.month, birthday.day)
    if today > next_birthday:
        next_birthday = datetime(today.year+1, birthday.month, birthday.day)
    delta = next_birthday - today
    print('age:',today.year-birthday.year)
    return delta.days
    
def main():
    birthday = datetime(1996, 6, 1)
    datetoday()
    delta = age_and_birthday(birthday)

if __name__ == '__main__':
    main()