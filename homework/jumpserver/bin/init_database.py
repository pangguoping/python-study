#!/usr/bin/env python
# -*-coding=utf-8-*-

import os, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)
from db.db_strut import *

#初始化数据库表结构
if __name__ == '__main__':
    init_db()