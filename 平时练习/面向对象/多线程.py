'''


import time
from threading import Thread

def do_thread(num):
    print('this is thread %s' %str(num))
    time.sleep(3)

for i in range(5):
    t = Thread(target=do_thread,args=(i,))
    t.start()
'''
'''

import time
from threading import Thread
def do_thread(num):
    print('this is thread %s' %str(num))
    time.sleep(2)
for i in range(2):
    t = Thread(target=do_thread,args=(i,))
    t.start()
    t.setName('Mythread_{0}'.format(str(i)))
    print(t.getName())
'''
'''

import time
from threading import Thread
def do_thread(num):
    print('this is thread %s' %str(num))
    time.sleep(3)
    #执行到此时主线程执行完成了，程序结束，下面的代码不会执行
    print('OK',str(num))

for i in range(2):
    t = Thread(target=do_thread,args=(i,))
    #设置线程为后台线程
    t.setDaemon(True)
    t.setName('Mythread_{0}'.format(str(i)))
    t.start()
    print(t.getName())
'''
'''

import time
from threading import Thread

def do_thread(num):
    time.sleep(3)
    print("this is thread %s" % str(num))


for i in range(2):
    t = Thread(target=do_thread, args=(i,))
    t.setName("Mythread_{0}".format(str(i)))
    t.start()
    t.join()
    print("print in main thread: thread name:", t.getName())
'''
'''

import time
import threading
def do_thread(num):
    global public_num
    #加锁
    lock.acquire()
    public_num -= 1
    #解锁
    lock.release()
    time.sleep(1)
    print('public_num in thread_%s is %s' %(str(num),str(public_num)))

public_num = 100
threads = []
lock = threading.Lock()
for i in range(50):
    t = threading.Thread(target=do_thread,args=(i,))
    t.setName('Mythread_{0}'.format(str(i)))
    t.start()
    threads.append(t)
#等待所有子线程结束
for t in threads:
        t.join()
print('last result of public_num is',public_num)

'''
'''

import threading

def do(event):
    print('start')
    #默认初始化状态为False,到这里就阻塞了
    event.wait()
    print('execute\n')
if __name__ == '__main__':
    event_obj = threading.Event()
    for i in range(10):
        t = threading.Thread(target=do,args=(event_obj,))
        t.start()
    inp = input('input>>>>:')
    if inp == 'true':
        #如果为True,则flag=True ，不阻塞，子进程继续运行
        event_obj.set()
    else:
        event_obj.clear()

'''
'''

import threading
import time

def light():
    linght_time = 0
    if not event.is_set():
        event.set()  # Flag = True, 阻塞
    while True:
        time.sleep(1)
        if linght_time < 10:
            print("Green is on....")
        elif linght_time < 13:
            print("Yellow is on ....")
        elif linght_time < 16:
            print("Red is on ......")
            if event.is_set():
                event.clear()
        else:    # 大于16, 该重新调绿灯了
            linght_time = 0
            event.set()

        linght_time += 1

def car_run(carnum):
    while True:
        time.sleep(2)
        if event.is_set():
            print("car %s is run" % carnum)
        else:
            print("CAR %s IS WAITTING........" % carnum)

if __name__ == "__main__":
    event = threading.Event()
    l = threading.Thread(target=light, )
    l.start()
    for i in range(3):
        c = threading.Thread(target=car_run, args=(str(i), ))
        c.start()

'''

import threading
import time

def do():
    semaphro.acquire()
    print('this is {0} set the semaphore'.format(threading.current_thread().getName()))
    time.sleep(2)
    semaphro.release()
    print("\033[1;30mthi is {0} release the semaphore\033[0m".format(threading.current_thread().getName()))

if __name__ == '__main__':
    semaphro = threading.Semaphore(2)
    for i in range(10):
        t = threading.Thread(target=do)
        t.setName("Thread_{0}".format(str(i)))
        t.start()
    print('finished')
















