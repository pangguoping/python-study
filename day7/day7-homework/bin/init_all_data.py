#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import sys,os,pickle
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf.setting import *
from core import manage_sys
from core import student

#将所有pickle数据库中的数据写入空列表
manage_sys.data_flush([])
manage_sys.subject_data_flush([])
student.student_data_flush([])
