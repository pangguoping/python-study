#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
#exchange 消费者
import pika
import sys
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.11.123',5672,'/',credentials))
channel = connection.channel()
channel.exchange_declare(exchange='logs_fanout',type='fanout')
message = '456'
channel.basic_publish(exchange='logs_fanout',routing_key='',body=message)
print('[x] Sent %r' % message)
connection.close()