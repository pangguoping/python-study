#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import pickle
from s1 import Foo
ret = pickle.load(open(db,'rb'))
print(ret)