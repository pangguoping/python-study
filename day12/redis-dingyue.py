#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
import redis-server
obj = redis-server.RedisHelper()
data = obj.subscribe('fm777')
print(data.parse_response())