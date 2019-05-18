# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:27:30 2019

@author: czfyy
"""

class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

def print_time(t):
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

def is_after(t1, t2):
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)

def increment(time, seconds):
    time.second += seconds 
    if (time.second % 60) >= 0:   #可以用divmod()
        time.minute += time.second//60
        time.second -= 60*(time.second//60)
        if (time.minute % 60) >= 0:
            time.hour += time.minute//60
            time.minute -= 60*(time.minute//60)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def main():
    time = Time()
    time.second = 0
    time.minute = 0
    time.hour = 0
    increment(time, 3601)
    print_time(time)
    
if __name__ == '__main__':
    main()