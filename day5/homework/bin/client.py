#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #day5-homework目录
#print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#  添加环境变量
sys.path.append(BASE_DIR)
from modules.login import login
if __name__ == '__main__':
    login()


