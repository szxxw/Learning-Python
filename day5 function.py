#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
写⼀个函数，获取列表中的成绩的平均值，和最大值

假设定义的函数名为 avg
"""

def avg(s):

    m = max(s)
    av = sum(s)/len(s)
    return ('最大值为%s'%m,'平均值为%s'%av)

re1 = avg(s=[2,3,5,6,9.0,7.7,65.8])
print(re1)

"""
写⼀个函数，获取未知长度的二维列表中每一行的成绩的平均值，和最大值

假设定义的函数名为 avg2
"""

def avg2(s):
    result = []

    for i in s:
       result.append(avg(i))

    return result

re = avg2(([2,5,6.6,8.8],[1,29,-19.44,89.89,97],[1,4,6,]))
print(re)





