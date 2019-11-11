#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
欢迎使用【学生信息管理系统】V1.0
请选择你想要进行的操作
1. 新建学生信息
2. 显示全部信息
3. 查询学生信息
4. 删除学生信息
5. 修改学生信息

0. 退出系统
'''


def huanying():
    print("*****" * 9)
    print("欢迎您使用【学生信息管理系统】V1.0")
    print("请选择你想要进行的操作")
    print('1. 新建学生信息', '2. 显示全部信息', '3. 查询学生信息', '4. 删除学生信息', '5. 修改学生信息','\n'
          '0. 退出系统','\n',sep="\n", end='')
    print("*****" * 9)


huanying()

def mainOperation():
    huanying()
    #list_info = []
    while True:

        a = input("请选择您的操作：")
        print('您选择的操作是{}'.format(a))
        if a == 0:
            print('退出系统')
            break
        elif a == 1:
            print("新建学生信息")

            pass
        elif a == 2:
            print("显示全部信息")

        elif a == 3:
            print("查询学生信息")

        elif a == 4:
            print("删除学生信息")

        elif a == 5:
            print("修改学生信息")



        else:
            print('输入错误请重新输入')

def xinjian():
    # 输入学生信息
    name = input("请输入姓名：")
    chinese = input("请输入语文成绩：")
    math = input("请输入数学成绩：")
    english = input("请输入英语成绩：")
    # 加完之后的总分是数字
    total = int(chinese) + int(math) + int(english)
    # 与类型无关 只要实现效果就行

    # 字典存储学生信息
    stu = {
        "name": name,
        "chinese": chinese,
        "math": math,
        "english": english,
        "total": total
    }
    global info_list #定义一个全局变量
    info_list = []
    info_list.append(stu)
    # 4. 提示添加成功信息
    print("成功添加 %s 的信息" % stu['name'])

def quanbu():
    print(info_list)

def chaxun():

   

