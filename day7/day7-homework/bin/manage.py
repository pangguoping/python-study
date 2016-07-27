#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import core.manage_sys

#管理员入口
if __name__ == '__main__':
    core.manage_sys.login()
    core.manage_sys.main()
