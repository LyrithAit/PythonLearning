#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input("Enter the number of students: "))
data = {}  # 用来存储数据的字典变量
Subjects = ('Physics', 'Maths', 'History')  # 所有科目

for i in range(0, n):
    name = input('Enter the name of the student {}: '.format(i + 1))  # 获得学生名称
    marks = []  # 创建分数列表
    for x in Subjects:
        marks.append(int(input('Enter marks of {}: '.format(x))))  # 获得每一科的分数并插入到列表
    data[name] = marks  # 创建键值对

for x, y in data.items():  # 遍历该字典
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")
