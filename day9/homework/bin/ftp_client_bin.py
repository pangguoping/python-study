#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import sys,os
BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
import module.ftp_client

if __name__ == '__main__':
    module.ftp_client.main()