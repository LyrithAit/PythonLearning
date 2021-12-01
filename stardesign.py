#!/usr/bin/env python3
# -*- coding: utf-8 -*-
row = int(input("Enter the number of rows: ")) # 星星递减
n = row
while n >= 0:
    x =  "*" * n
    print(x)
    n -= 1

'''
n = int(input("Enter the number of rows: ")) # 星星递增
i = 1
while i <= n:
    print("*" * i)
    i += 1

row = int(input("Enter the number of rows: ")) # 星星递减 (右端对齐)
n = row
while n >= 0:
    x = "*" * n
    y = " " * (row - n)
    print(y + x)
    n -= 1
'''