#!/usr/bin/env  python
# -*- coding:utf-8 -*-

import s4
s4.login()
import lib.common
lib.common.f1()

import sys
for item in sys.path:
    print(item)

from s4 import login
#from s4 import *
login()

from lib import common as lib_comm

