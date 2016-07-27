#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

import pika
import sys
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.199.181',56720,'/',credentials))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs_test_1',type='direct')
severity = 'error'
message = '123'
channel.basic_publish(exchange='direct_logs_test_1',routing_key=severity,body=message)
print('[x] Sent %r:%r' %(severity,message))
connection.close()