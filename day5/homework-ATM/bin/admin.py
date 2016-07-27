#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src import admin as src_admin

if __name__ == '__main__':
    src_admin.run()
