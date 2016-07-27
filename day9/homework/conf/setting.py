#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import sys
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

#用户信息文件
#user_data_file = '%s%sdata%suser.json'%(BASEDIR,os.sep,os.sep)
user_data_file = os.path.join(BASE_DIR, "data/user.json")
#用户家目录
#user_document = '%s%sdocument'%(BASEDIR,os.sep)
user_document = os.path.join(BASE_DIR, "document")
#下载目录
download_document = os.path.join(BASE_DIR, "download")
