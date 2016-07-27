#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping

import sys,os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import core.student
#学生系统入口，注册登录
if __name__ == '__main__':
    core.student.main()
