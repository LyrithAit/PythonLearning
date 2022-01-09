#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def view_dir(path='.'):
    names = os.listdir(path)
    names.sort()
    for name in names:
        print(name, end =' ')
    print()
