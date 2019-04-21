# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 14:00:14 2019

@author: czfyy
"""

import turtle

'''
每一条koch曲线的生成方式与雪花一瓣的生成方式相同
因此koch函数是可以复用的
先将给定长度n反复除以3求得小于十的最小整数，具体见控制台输出
一个7.40代表一个小尖和两个横，四个7.40（即出现一个22.2）代表一个星星形状的，
一个66.6代表一瓣的四分之一
函数体反复调用了16次
'''
def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    print(m)
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)


def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)


bob = turtle.Turtle()

bob.pu()
bob.goto(-300, 90)
bob.pd()
snowflake(bob,600)

turtle.mainloop()
