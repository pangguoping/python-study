#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
'''


class People(object):

    def __init__(self,name):
        self.name = name

    def talk(self):
        print('my name is {0}'.format(self.name))

zhangsan = People('zhangsan')
zhangsan.talk()
'''
'''

class People(object):
    color = 'red'

    def __init__(self,name):
        self.name = name
        self.__talk()

    def __talk(self):
        print('my name is {0},color is {1}'.format(self.name,self.color))

zhangsan = People('zhangsan')

'''

'''
class People(object):
    color = 'red'

    def __init__(self, name):
        self.name = name
        self.__talk()

    def __talk(self):
        print("my name is {0}, color is {1}".format(self.name, self.color))
    def show_job(self):
        print(" No job")

class Teacher(People):
    def __init__(self, name, age):
        super(Teacher, self).__init__(name)
        self.age = age
        self.__talk()

    def __talk(self):
        print("I'm Tearcher,  I'm {0}".format(self.age))
    def show_job(self):
        print(" Teacher")

zhangsan = Teacher("zhangsan",20)
zhangsan.show_job()

'''

'''

class Father():
    def show(self):
        print("show in Father")

class Son_1(Father):
    def __init__(self):
        pass

class Son_2(Father):
    def show(self):
        print("show in Son_2")

class subSon(Son_1,Son_2):
    def __init__(self):
        pass

p = subSon()
p.show()
'''

class Father(object):
    def show(self):
        print("show in Father")

class Son_1(Father):
    def __init__(self):
        pass

class Son_2(Father):
    def show(self):
        print("show in Son_2")


class subSon(Son_1,Son_2):
    def __init__(self):
        pass

p = subSon()
p.show()















