#!/usr/bin/env python3
import sys

def Hours(minute):
    if minute < 0:
        raise ValueError("Input number cannot be negative")
    else:
        print("{} H, {} M".format(int(minute / 60), minute % 60))

try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")
