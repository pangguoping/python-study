import threading,time,queue

class ThreadPool:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self._q=queue.Queue(maxsize)
        for i in range(maxsize):
            self._q.put(threading.Thread)

    def get_thread(self):
        return self._q.get()
    def add_thread(self):
        self._q.put(threading.Thread)

pool=ThreadPool(5)

def task(arg,p):
    print(arg)
    time.sleep(1)
    p.add_thread()

for i in range(100):
    t = pool.get_thread()   #线程池中没有线程为阻塞状态
    obj=t(target=task,args=(i,pool))
    obj.start()