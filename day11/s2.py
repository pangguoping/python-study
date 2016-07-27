#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
#队列
'''


import queue
#先进先出队列
#put放数据,block是否阻塞,timeout = 阻塞时的超时时间
#get 取数据,默认阻塞。block是否阻塞,timeout阻塞时的超时时间
#队列最大长度
#qsize()真实个数
#maxsize 支持最大个数
#q.get()执行完成后,执行q.task_done()告诉队列取值完成
#join,task_done ,阻塞进程,当队列中任务执行完毕之后,不再阻塞
#q = queue.Queue(2)  #可以加参数,表示队列最大个数
q = queue.Queue(2)
q.put(11)
q.put(22)
#q.put(33,timeout=2)  #阻塞2秒,如果2s后还是无法插入队列,然后直接报错
#q.put(33,block=False)   #block=False 表示不阻塞,如果不能插入队列,然后直接报错

print(q.qsize())  #获取队列的个数
#print(q.qsize())
print(q.get())
print(q.get())
#print(q.get(timeout=10))  #默认阻塞,block是否阻塞,timeout=10 表示阻塞超时时间
#print(q.get(block=False))


#队列分类


#2.后进先出
import queue
q = queue.LifoQueue()
q.put(123)
q.put(456)
print(q.get())
print(q.get())

'''

#3.优先级队列
import queue
q = queue.PriorityQueue()
q.put((0,"test1"))
q.put((3,"test3"))
q.put((4,"test4"))
print(q.get())
print(q.get())
print(q.get())

#4.双向队列
import queue
q = queue.deque()
q.append(123)
q.append(444)
q.appendleft(555)
print(q.pop())
print(q.pop())
print(q.popleft())
