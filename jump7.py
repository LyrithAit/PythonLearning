#!/usr/bin/env python3
for a in range (1,101):
    if a % 7 == 0:
        continue
    elif a % 10 == 7:
        continue
    elif a // 10 == 7:
        continue
    else:
        print(a)

'''code use while
a = 0
while a < 100:
    a = a + 1
    if a % 7 == 0 or a % 10 == 7 or a // 10 == 7:
        continue
    else:
        print(a)
'''