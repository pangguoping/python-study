#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import hashlib
obj = hashlib.md5(bytes('sdflsdfsdf',encoding='utf-8'))
obj.update(bytes('123',encoding='utf-8'))
result = obj.hexdigest()
print(result)
