#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
import os,sys,time
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
#配置文件

#存放老师信息的数据文件
manage_data_file='%s/data/manage.pickle'%BASE_DIR
#课程信息数据文件
subject_data_file='%s/data/subject.pickle'%BASE_DIR
#学生信息的数据文件
student_data_file='%s/data/student.pickle'%BASE_DIR

#定义教师类
class Teacher:
    def __init__(self, name, age, favor):
        self.favor = favor
        self.name = name
        self.age = age
        self.asset = 0

    def gain(self, value):
        """
        上课增加资产
        :param value:
        :return:
        """
        self.asset = int(self.asset) + int(value)

    def teach_accidents(self):
        """
        出现课程事故减少资产
        :return:
        """
        self.asset -= 1
from core import manage_sys
#课程类
class Subject:
    def __init__(self,classes,value,teacher_name):#构造方法
        self.classes=classes
        self.value=int(value)
        self.teacher_name=teacher_name
    def attend_class(self):
        #上课增加老师资产
        print('来上课,今天我们学%s' % self.classes)
        print(5 * ('%s...' % self.classes))
        time.sleep(1)
        teacher_obj, index = manage_sys.sub_match_teacher(self.classes)
        teacher_obj.gain(self.value)
        teacher_data = manage_sys.data_read()
        teacher_data[index] = teacher_obj
        manage_sys.data_flush(teacher_data)

    def accidents(self):
        """
        课堂事故，减少老师资产
        :return:
        """
        print('今天上不了,%s老师来事了休息' % self.teacher_name)
        teacher_obj, index = manage_sys.sub_match_teacher(self.classes)
        teacher_obj.teach_accidents()
        teacher_data = manage_sys.data_read()
        teacher_data[index] = teacher_obj
        manage_sys.data_flush(teacher_data)

#定义学生类
class Student:
    def __init__(self,name,pwd):
        self.name=name
        self.pwd=pwd
        self.subject_classes=[]


