#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:123@192.168.11.139:3306/s13", max_overflow=5)

Base = declarative_base()
#创建单表
class Test(Base):
    __tablename__ = 'test'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(32))

#创建一对多表
class Group(Base):
    __tablename__ = 'group'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    caption = Column(String(32))
class User(Base):
    __tablename__ = 'user'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(32))
    group_id = Column(Integer,ForeignKey('group.nid'))
    group = relationship("Group",backref='uuu')
    def __repr__(self):
        temp = '%s - %s:%s' %(self.nid,self.username,self.group_id)
        return temp
def init_db():
    Base.metadata.create_all(engine)
#init_db()


Session = sessionmaker(bind=engine)
session = Session()
#向group表中添加数据
# session.add(Group(caption='dba'))
# session.add(Group(caption='ddd'))
# session.commit()

#向user表中添加数据
# session.add_all([
#     User(username='alex1',group_id=1),
#     User(username='alex2',group_id=2)
# ]
# )
# session.commit()

#只是获取用户
ret = session.query(User).filter(User.username == 'alex1').all()
print(ret)
ret = session.query(User).all()
obj = ret[0]
print(ret)
print(obj)
print(obj.nid)
print(obj.username)
print(obj.group_id)


'''

#正向查询

#原始方式:
ret = session.query(User.username,Group.caption).join(Group,isouter=True).all()
print(ret)
#使用group,relation
#新式正向查询
ret = session.query(User).all()
for obj in ret:
    print(obj.nid,obj.username,obj.group,obj.group_id,obj.group.nid,obj.group.caption)
#反向查询
#原始方式
ret = session.query(User.username,Group.caption).join(Group,isouter=True).filter(Group.caption == 'DBA').all()
print(ret)
#新式方向查询
obj = session.query(Group).filter(Group.caption == 'DBA').first()
print(obj.nid)
print(obj.caption)
print(obj.uuu)

'''





