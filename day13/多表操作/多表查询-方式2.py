#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:123@192.168.11.139:3306/s13", max_overflow=5)

Base = declarative_base()
class Host(Base):
    __tablename__ = 'host'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(32))
    port = Column(String(32))
    ip = Column(String(32))

class HostUser(Base):
    __tablename__ = 'host_user'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(32))
#创建第一张表和第二张表的关系表
class HostToHostUser(Base):
    __tablename__ = 'host_to_host_user'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    host_id = Column(Integer,ForeignKey('host.nid'))
    host_user_id = Column(Integer,ForeignKey('host_user.nid'))

    host = relationship('Host',backref = 'h')
    host_user = relationship('HostUser',backref = 'u')



Session = sessionmaker(bind=engine)
session = Session()
# host_obj = session.query(Host).filter(Host.hostname=='c1').first()
# print(host_obj)  #输出 <__main__.Host object at 0x103760e10>
# print(host_obj.nid)   # 输出1
# print(host_obj.hostname)   #c1
# #第三表对应的对象
# print(host_obj.h)
# #循环获取第三张表对应的对象
# for item in host_obj.h:
#     print(item.host_user,item.host_user.nid,item.host_user.username)


host_obj = session.query(Host).filter(Host.hostname=='c1').first()
for item in host_obj.h:

    print(item.host_user.username)
