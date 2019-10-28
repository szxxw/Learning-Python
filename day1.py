#!/usr/bin/env python
# -*- coding: utf-8 -*-
#check all the keywords of python
# import keyword
# for i in keyword.kwlist:
#     print(i)
#alt+shift+enter run/execute all the commands

#Define a function to calculate BMI indexes
def BMI():
    weight = float(input("Please input your weight(kilogram):"))
    height = float(input("Please input your height(meter):"))
    BMIindex = round(weight/(height)**2,2)
    result = print("Your BMI index is "+str(BMIindex)+" (The result reserves two decimal fractions)")
    return result

BMI()
# C:\Users\21024\python3.6\python.exe "D:/python exercises for beginners/day1.py"
# Please input your weight(kilogram):80.99
# Please input your height(meter):1.98
# Your BMI index is 20.66 (The result reserves two decimal fractions)
#
# Process finished with exit code 0

#Variable's location
a = 10
b = 10
id(b)
id(a)#same
#identify the location of variables by method (is/is not)
a is b
a is not b
