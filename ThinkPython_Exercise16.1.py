# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:14:09 2019

@author: czfyy
"""

from ThinkPython_Exercise16 import *

def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def time_to_int(time):
    """Computes the number of seconds since midnight.

    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def mul_time(t, factor):
    if not valid_time(t):
        raise ValueError('invalid Time object in add_time')
    seconds = time_to_int(t) * factor
    return int_to_time(seconds)