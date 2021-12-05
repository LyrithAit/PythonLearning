#!/usr/bin/env python3
# -*- coding: utf-8 -*-
a, b = 0, 1  # 初始化 a 和 b
while b < 100:
    print(b, end=' ')
    a, b = b, a + b  # 从右往左赋值, 将 a + b 的值赋值给 b, b 的值赋值给 a
print()
