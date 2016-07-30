#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123@192.168.1.103:3306/test", max_overflow=5)

Base = declarative_base()



#定义初始化数据库函数
def init_db():
    Base.metadata.create_all(engine)

#顶固删除数据库函数
def drop_db():
    Base.metadata.drop_all(engine)

# drop_db()
# init_db()

#创建mysql操作对象
Session = sessionmaker(bind=engine)
session = Session()

obj = Users(name='alex',extra='sb')
session.add(obj)
#add_all 列表形式
session.add_all([
    Users(name='cc',extra='cow'),
    Users(name='dd',extra='cowcow')
])
#提交
session.commit()