#!/usr/bin/env python3
with open('/proc/cpuinfo') as f:
    s = f.read()
    res = ""

    for char in s:
        if char.isdigit():
            res += char
    print(res)
