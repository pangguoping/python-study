#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: pangguoping  4008167189
#简单继承
class F1:  #父类，或者基类
    def show(self):
        print('F1.show')

class F2(F1):  #表示F2继承F1。F2叫子类，或者派生类
    def bar(self):
        print('bar')

obj = F2()
obj.show()
obj.bar()

#父类和子类有相同的方法，优先执行子类中的方法
class F1:  #父类，或者基类
    def show(self):
        print('F1.show')

class F2(F1):  #表示F2继承F1。F2叫子类，或者派生类

    def bar(self):
        print('bar')
    def show(self):   #子类优先级高
        print('F2.show')

obj = F2()
obj.show()
obj.bar()

#子类中封装数据，父类中也可以访问
class F1:  #父类，或者基类
    def show(self):
        print('F1.show')
    def foo(self):
        print(self.name)

class F2(F1):  #表示F2继承F1。F2叫子类，或者派生类
    def __init__(self,name):
        self.name = name

    def bar(self):
        print('bar')


obj = F2('xiaoming')
obj.foo()    #输出是xiaoming ， 继承就相当于把父类的方法放到了子类中，所以这里输出的是xiaoming

#复杂继承
class S1:
    def F1(self):
        self.F2()  #此时的self相当于对象obj
    def F2(self):
        print('S1.F2')

class S2(S1):
    def F3(self):
        self.F1()
    def F2(self):
        print('S2.F2')

obj = S2()
obj.F3()
#输出是S2.F2  ， 执行过程：执行S2类中的F3方法时，会去执行self.F1()方法，因为S2中没有该方法，所以去父类中寻找，父类有该方法，
# 那么就执行父类中的F1()方法，在执行F1()方法时，会执行self.F2()。因为继承的本质是把父类的方法复制到子类中，
# 所以def F1(self):self.F2() 放到了S2类中，因为S2类中有F2方法，所以执行S2类中的F2()方法。子类和父类有相同的方法时，子类方法优先级高。

#只要到self.F2()这样的时候，直接回到原点寻找。例如该例子中应该回到S2类中寻找F2()方法，
# 发现子类S2中有该方法，那么直接执行。如果S2类中没有，那么去父类中寻找F2()方法
