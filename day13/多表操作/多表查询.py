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


Session = sessionmaker(bind=engine)
session = Session()

#查询
#1、旧方式:
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
#host_boj.nid
#2)、所有用户ID
host_2_host_user = session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id == host_obj.nid).all()
#print(host_2_host_user)  #输出 [(1,), (2,), (3,)]
#把列表元祖转换成列表
r = zip(*host_2_host_user)
#print(list(r))   #输入 [(1, 2, 3)]
#print(list(r)[0])   #输出  (1, 2, 3)
#3)、根据用户ID找到所有用户
users = session.query(HostUser.username).filter(HostUser.nid.in_(list(r)[0])).all()
print(users)


