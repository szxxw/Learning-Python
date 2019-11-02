#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
输入三个数，按照其大小顺序先后打印

1. 使用input输入三个数
2. 判断三个数的大小然后排序
3. 将三个数按顺序输出
"""

nums = []
for i in range(1,4):
    nums.append(float(input('请输入第{}个数：'.format(i))))
nums.sort(reverse=True)
print(nums)


"""
计算 0 ~ 100 之间 所有 偶数 的累计求和结果

开发步骤

1. 编写循环确认要计算的数字 
2. 添加结果变量，在循环内部处理计算结果 
"""
s = 0
for i in range(101):
    if 0==i%2:
        s+=i
    else:
        pass

print(s)

"""
打印一百以内的素数
质数定义为在大于1的自然数（到无穷大的整数）中，除了1和它本身以外不再有其他因数。

1. 打印0-100的所有数字
2. 判断当数字是否是素数
	+ 如果是素数就打印
	+ 如果不是素数就什么都不做
"""
num = []
for i in range(2,101):
    for j in range(2,i):
        if 0==i%j:
            break

    else:
        num.append(i)
print(num)

for i in range(2,2):
    print(i)



'''
附加题：

用for语句实现九九乘法表 
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end="\t")
    print()