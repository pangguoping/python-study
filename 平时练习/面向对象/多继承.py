#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping
#1、简单的多继承
class C0:
    def f1(self):
        print('C0_f1')
class C1(C0):

    def f2(self):
        print('C1_f2')

class C2:
    def f2(self):
        print('C2_f2')

class C3(C2,C1):   #从左到右继承，左边的优先级高
    def f3(self):
        pass

obj = C3()
obj.f2()    #输出C2_f2

#2、复杂的多继承
class C0:
    def f2(self):
        print('C0_f1')
class C1(C0):

    def f1(self):
        print('C1_f2')

class C2:
    def f2(self):
        print('C2_f2')

class C3(C1,C2):   #从左到右继承，左边的优先级高
    def f3(self):
        pass

obj = C3()
obj.f2()    #输出C0_f1

#3、复杂继承关系
class C_2:
    def f2(self):
        print('C_2_f2')
class C_1(C_2):
    def f2(self):
        print('C_1_f2')
class C0(C_2):
    def f1(self):
        print('C0_f2')
class C1(C0):

    def f1(self):
        print('C1_f2')

class C2(C_1):
    def f2(self):
        print('C2_f2')

class C3(C1,C2):   #从左到右继承，左边的优先级高
    def f3(self):
        pass

obj = C3()
obj.f2()    #输出C0_f1