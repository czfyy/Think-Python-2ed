# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:38:18 2019

@author: czfyy
"""

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
   
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        elif isinstance(other, int):
            return self.increment(other)
    
    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
    
    def time_to_int(self):
        """Computes the number of seconds since midnight.
        time: Time object.
        """
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        print(seconds)
        return seconds
    
    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    

def int_to_time(seconds):
    """Makes a new Time object.

    seconds: int seconds since midnight.
    """
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    time = Time(hour, minute, second)
    return time

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)
    
    def __add__(self, other):
       if isinstance(other, Point):
           return self.add_point(other)
       elif isinstance(other, tuple):
           return self.add_tuple(other)
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def add_point(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def add_tuple(self, other):
        return Point(self.x + other[0], self.y + other[1])

def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

def main_time():
    start = Time(9, 45, 00)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print('Is end after start?')
    print(end.is_after(start))

    print('Using __str__')
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3])
    print(total)
    print_attributes(total)

def main_point():
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1)
    print(p2)
    print(p1 + p2)
    print(p1 + (3, 4))
    print((3, 4) + p1)
    
if __name__ == '__main__':
    main_time()
    print()
    main_point()