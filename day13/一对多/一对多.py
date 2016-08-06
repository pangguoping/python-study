#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:123@192.168.29.128:3306/s13", max_overflow=5)

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
    #这个方法输出什么，对象就获取什么
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
# session.add(Group(caption='sa'))
# session.commit()
#
# #向user表中添加数据
# session.add_all([
#     User(username='user1',group_id=1),
#     User(username='user2',group_id=1),
#     User(username='user3', group_id=2),
#     User(username='user4', group_id=2)
# ]
# )
# session.commit()
####################################### 单表查询 ############################################
#只是获取用户
# ret = session.query(User).filter(User.username == 'user1').all() #这里获取的是对象
# print(ret)
# ret = session.query(User).all()
# obj = ret[0]
# print(ret)
# print(obj)
# print(obj.nid)
# print(obj.username)
# print(obj.group_id)
#######################
#这里获取的是列表
# ret = session.query(User.username).all()  #这是映射的方式
# print(ret)

############################### 多表查询 #######################################
# ret = session.query(User).join(Group).all()   #或者.filter()
# #select * from user left join group on user.group_id = group.nid
# print(ret)
# #查看生成的sql
# sql = session.query(User).join(Group)
# print(sql)
# #以left.join查看
# ret = session.query(User).join(Group,isouter=True).all()
# print(ret)
# sql = session.query(User).join(Group,isouter=True)
# print(sql)
#
# #映射方式
sql = session.query(User.username,Group.caption).join(Group,isouter=True)
print(sql)
ret = session.query(User.username,Group.caption).join(Group,isouter=True).all()
print(ret)  # [('user1', 'dba'), ('user2', 'dba'), ('user3', 'sa'), ('user4', 'sa')]

# ret = session.query(User).all()
# for obj in ret:
#     print(obj.nid,obj.username,obj.group,obj.group_id,obj.group.nid,obj.group.caption)
#out:

# ret = session.query(User.username,Group.caption).join(Group,isouter=True).filter(Group.caption == 'DBA').all()
# print(ret)
# #新方式（反向查询）
# obj = session.query(Group).filter(Group.caption == 'DBA').first()
# print(obj.uuu)
'''

#正向查询

#原始方式:
ret = session.query(User.username,Group.caption).join(Group,i
souter=True).all()
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
print(obj.uuu)

'''





