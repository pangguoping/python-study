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

def init_db():
    Base.metadata.create_all(engine)

#init_db()

Session = sessionmaker(bind=engine)
session = Session()

#向表中添加数据
#1、向Host表中添加数据
# session.add_all([
#     Host(hostname='c1',port='22',ip='1.1.1.1'),
#     Host(hostname='c2',port='22',ip='1.1.1.2'),
#     Host(hostname='c3',port='22',ip='1.1.1.3'),
#     Host(hostname='c4',port='22',ip='1.1.1.4'),
#     Host(hostname='c5',port='22',ip='1.1.1.5'),
# ])
# session.commit()

#2、向HostUser中添加数据
# session.add_all([
#     HostUser(username='root'),
#     HostUser(username='db'),
#     HostUser(username='nb'),
#     HostUser(username='sb'),
# ])
# session.commit()

#3、向HostToHostUser表中添加数据
session.add_all([
    HostToHostUser(host_id=1,host_user_id=1),
    HostToHostUser(host_id=1,host_user_id=2),
    HostToHostUser(host_id=1,host_user_id=3),
    HostToHostUser(host_id=2,host_user_id=2),
    HostToHostUser(host_id=2,host_user_id=4),
    HostToHostUser(host_id=2,host_user_id=3),
])
session.commit()