#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import sys
import os
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
#obj = __import__("ooo")
obj = __import__("lib.commons",fromlist=True)
obj.login()

