#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
#exchange-key-publish 生产者
import pika
import sys
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.11.123',5672,'/',credentials))
channel = connection.channel()
channel.exchange_declare(exchange='direct_logs_test_1',type='direct')
severity = 'error'
message = '123'
channel.basic_publish(exchange='direct_logs_test_1',routing_key=severity,body=message)
print('[x] Sent %r:%r' %(severity,message))
connection.close()