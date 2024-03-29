#!/usr/bin/env python
# -*- coding: utf-8 -*-
#task1
"""
s =  'hello world !'

1. 截取从 0 ~ 5 位置 的字符串
2. 截取从 5 ~ 末尾 的字符串
3. 截取从 开始 ~ 5 位置 的字符串
4. 截取完整的字符串
5. 从开始位置，每隔一个字符截取字符串
6. 从索引 1 开始，每隔一个取一个
7. 截取从 2 ~ 末尾 - 1 的字符串
8. 截取字符串末尾两个字符
"""
s = 'hello world !'
print(s[:6])
print(s[5:])
print(s[:6])
print(s[::])
print(s[::2])
print(s[1::2])
print(s[2:-1])
s = 'hello world !'
print(s[-1:-4:-1])

#task 2

"""
在不修改 i 的情况下，输出001。
"""
i = 1
print("00{}".format(i))
print("00%d"%(i))
print("00"+f"{i}"

j=1
print("{:0>3}".format(j))
print('%03d'%(j))
print(f"{j:0>3}")
"""
请用你字符串格式化的代码，输出以下结果

python 是一门动态解释型语言，起源于1989年圣诞节期间
Java 是一门静态编译型语言，起源于1991年
C 是一门静态编译型语言，起源于1969年到1973年期间
"""
print(
'%s是一门动态解释型语言，起源于%s'%("python",'1989年圣诞节期间\n'),
'%s是一门静态编译型语言，起源于%s\n'%('java','1991年'),
'%s是一门静态编译型语言，起源于%s\n'%("C",'1969年到1973年期间')
)

mystr = '{}是一门{}语言，起源于{}年{}'
print(mystr.format('Python','动态解释型',1989,'圣诞节期间'))
print(mystr.format('Java','静态编译型语言',1991,''))
print(mystr.format('C','静态编译型语言','1969','到1973年期间'))


# python是一门动态解释型语言，起源于1989年圣诞节期间
#  java是一门静态编译型语言，起源于1991年
#  C是一门静态编译型语言，起源于1969年到1973年期间

# 作业三
#
# 1. 实现一个加法计算器，可以接受用户输入的数据，然后计算其相加的结果
#
# 2. 有一个变量a = '12.3',想要将其转换为整型，可以怎么做

def add():
    a = float(input('请输入数字a:'))
    b = float(input('请输入数字b:'))
    print(a+b)
add()

#方法1
a = '12.3'
b = int(float(a))
print(b)
#方法2
a = '12.3'
print(float(eval(a)))