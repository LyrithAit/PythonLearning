#!/usr/bin/env python3
with open('/proc/cpuinfo') as fobj:
    for line in fobj:
        print(line, end = '')
