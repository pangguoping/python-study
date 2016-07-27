#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
#1、获取所有节点
import configparser
config = configparser.ConfigParser()
config.read('db',encoding='utf-8')
ret = config.sections()
print(ret)
#2、获取指定节点下所有的键值对
import configparser
config = configparser.ConfigParser()
config.read('db',encoding='utf-8')
ret = config.items('section1')
print(ret)
#3、获取指定节点下所有的建
import configparser
config = configparser.ConfigParser()
config.read('db',encoding='utf-8')
ret = config.options('section1')
print(ret)
#4、获取指定节点下指定key的value值
import configparser
config = configparser.ConfigParser()
config.read('db',encoding='utf-8')
v = config.get('section1','k1')
#v = config.getint('section1','k1')
# v = config.getfloat('section1', 'k1')
# v = config.getboolean('section1', 'k1')
print(v)
#5、检查、删除、添加节点
import configparser
config = configparser.ConfigParser()
config.read('db',encoding='utf-8')

#检查
has_sec = config.has_section('section1')
print(has_sec)
#添加节点
config.add_section('SEC_1')
config.write(open('db','w'))
#删除节点
config.remove_section('SEC_1')
config.write(open('db','w'))

#6、检查、删除、设置指定组内的键值对
import configparser
config = configparser.ConfigParser()
config.read('db',encoding='utf-8')
#检查
has_opt = config.has_option('section1','k1')
print(has_opt)
#删除
has_opt = config.has_option('secion1','k1')
print(has_opt)
#设置
config.set('section1','k10','123')
config.write(open('db','w'))

