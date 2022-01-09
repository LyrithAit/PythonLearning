#!/usr/bin/env python3
import sys
try:
    i = int(sys.argv[1])
    print("{} H, {} M".format(int(i / 60), i % 60))
except:
    print("Parameter Error")
