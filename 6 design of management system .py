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
students_list = [
    {'name': '李四', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '王五', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '张三', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
]




def huanying():
    print("*****" * 9)
    print("欢迎您使用【学生信息管理系统】V1.0")
    print("请选择你想要进行的操作")
    print('1. 新建学生信息', '2. 显示全部信息', '3. 查询学生信息', '4. 删除学生信息', '5. 修改学生信息','\n'
          '0. 退出系统','\n',sep="\n", end='')
    print("*****" * 9)




def mainOperation():
    huanying()
    #list_info = []
    while True:
        a = int(input("请选择您的操作："))
        print('您选择的操作是{}'.format(a))
        if a == 0:
            print('退出系统')
            break
        elif a == 1:
            print("新建学生信息")
            xinjian()
            #break


        elif a == 2:
            print("显示全部信息")
            quanbu()
            #break

        elif a == 3:
            print("查询学生信息")
            chaxun()
            #break

        elif a == 4:
            print("删除学生信息")
            shanchu()
            #break


        elif a == 5:
            print("修改学生信息")
            xiugai()
            #break



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

    students_list.append(stu)
    # 4. 提示添加成功信息
    print("成功添加 %s 的信息" % stu['name'])
    print(students_list)

def quanbu():
    # 从列表里面取出学生信息
    print("姓名\t\t语文\t\t数学\t\t英语\t\t总分")
    str_format = "{}\t\t{}\t\t{}\t\t{}\t\t{}"
    for stu in students_list:
        print(str_format.format(*stu.values()))
    print(students_list)


def shanchu():

    name  = input("请输入删除学生的姓名：")
    for stu in  students_list:
        if name == stu['name']:
            del students_list[students_list.index(stu)]
            break
        else:
            print('请重新输入名字：')
    print(students_list)

def chaxun():
    name = input("请输入需要查询的学生姓名:")

    # 去整体的内容里面去找
    for stu in students_list:
        # 判断学生姓名是否存在于已有的数据中
        # 存在于列表 是正常的 不存在与列表中也是正常的
        if name == stu["name"]:
            print("姓名\t\t语文\t\t数学\t\t英语\t\t总分")
            print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(*stu.values()))
            # 找到内容之后 跳出 for ... else ... 的整体
            break

    # 在student_list中的所有数据中找不到
        else:
            print("此学生不存在，请重新查询")
    print(students_list)



def xiugai():
    name = input("请输入想要修改的学生的名字：")
    for stu in students_list:
        if name == stu["name"]:
            # 不输入内容 则不修改
            print("(输入为空则不修改)")
            name = input("请输入姓名：")
            if name:
                stu["name"] = name
            chinese = input("请输入语文成绩：")
            if chinese:
                stu["chinese"] = chinese
            math = input("请输入数学成绩：")
            if math:
                stu["math"] = math
            english = input("请输入英语成绩：")
            if english:
                stu["english"] = english
            stu['total'] = int(stu["chinese"]) + int(stu["math"]) + int(stu["english"])
            break
    print(students_list)

mainOperation()





