# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:30:40 2019

@author: czfyy
"""

import time 
import calendar

print('当前时间戳为：',time.time())

localtime = time.localtime(time.time())
print('默认格式：',time.asctime(localtime))
print('格式一：',time.strftime('%Y-%m-%d %H:%M:%S',localtime))    # %Y-%m-%d %H:%M:%S为格式
type2 = time.strftime('%a %b %d %H:%M:%S %Y',localtime)         #手动配置成默认格式asctime（）
print('格式二：',type2)
print(time.mktime(time.strptime(type2,'%a %b %d %H:%M:%S %Y')),'\n')  #将type2格式的时间转为时间戳
       
cal = calendar.month(2019,3)                                                          #注意strp函数的参数的前后顺序
print('输出2019年3月日历：\n',cal)


'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''