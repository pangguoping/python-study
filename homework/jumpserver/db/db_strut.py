#!/usr/bin/env python
# -*-coding=utf-8-*-

from sqlalchemy import create_engine, and_, or_, func, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, DateTime
from  sqlalchemy.orm import sessionmaker, relationship

#测试前需要修改用户名密码,以及数据库名称
engine = create_engine("mysql+pymysql://root:123@192.168.29.128:3306/s13", max_overflow=5)
Base = declarative_base()  # 生成一个SqlORM 基类


class UserProfile2HostUser(Base):
    __tablename__ = 'userprofile_2_hostuser'
    id = Column(Integer, primary_key=True, autoincrement=True)
    userprofile_id = Column(Integer, ForeignKey('user_profile.id'),primary_key=True)
    hostuser_id = Column(Integer, ForeignKey('host_user.id'),primary_key=True)
    # userprofile = relationship('UserProfile',secondary=lambda :)


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)


class HostUser(Base):
    __tablename__ = 'host_user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    AuthTypes = [
        (u'ssh-passwd', u'SSH/Password'),
        (u'ssh-key', u'SSH/KEY'),
    ]
    auth_type = Column(String(64))
    username = Column(String(64), nullable=False)
    password = Column(String(255))
    host_id = Column(Integer, ForeignKey('host.id'))
    host = relationship('Host', backref='host_user')
    __table_args__ = (UniqueConstraint(u'host_id', u'username', name='_host_username_uc'),)

class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True, nullable=False)


class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)

    group_id = Column(Integer, ForeignKey('group.id'))

 #   hostid_list = relationship('HostUser', secondary=lambda :UserProfile2HostUser.__table__, backref='userprofiles')



#日志表
class Log(Base):
    __tablename__ = 'log'
    id = Column(Integer, primary_key=True)
    userprofile_id = Column(Integer, ForeignKey('user_profile.id'))
    hostuser_id = Column(Integer, ForeignKey('host_user.id'))
    cmd = Column(String(255))
    date = Column(DateTime)




# ss = Session()
# 定义初始化数据库函数
def init_db():
    Base.metadata.create_all(engine)


init_db()

# 删除数据库函数
def drop_db():
    Base.metadata.drop_all(engine)


# drop_db()


# 实例化数据库操作对象为session
Session = sessionmaker(bind=engine)
ss = Session()

###添加测试数据
ss.add_all([
    Group(id=1, name='DBA'),
    Group(id=2, name='SA')
])

ss.add_all([
    UserProfile(id=1,username='chengc',group_id=2),
    UserProfile(id=2,username='root',group_id=2)
])

ss.add_all([
    Host(id=1,hostname='test',ip_addr='192.168.4.193',port=22),
    Host(id=2,hostname='zhongrt1',ip_addr='1.1.1.1',port=22)
])

ss.add_all([
    HostUser(id=1,auth_type='pwd',username='root',password='7ujm8ik,',host_id=1),
    HostUser(id=2,auth_type='pwd',username='root',password='asdf',host_id=2)
])

ss.add_all([
    UserProfile2HostUser(userprofile_id=1,hostuser_id=1),
    UserProfile2HostUser(userprofile_id=2,hostuser_id=1)
])
#
ss.add_all([Group(id=3,name='SB')])
ss.commit()
