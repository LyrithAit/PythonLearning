#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Person(object):

    def __init__(self, name):  # 返回具有给定名称的 Person 对象
        self.name = name

    def get_details(self):  # 返回包含人名的字符串
        return self.name


class Student(Person):

    def __init__(self, name, branch, year):  # 返回 Student 对象, 采用 name, branch, year 3 个参数
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):  # 返回包含学生具体信息的字符串
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)


class Teacher(Person):
    
    def __init__(self, name, papers):  # 返回 Teacher 对象, 采用字符串列表作为参数
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))


person1 = Person('Sachin')
student1 = Student('Kushal', 'CSE', 2005)
teacher1 = Teacher('Prashad', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())
