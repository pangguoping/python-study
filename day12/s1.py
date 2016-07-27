#!/usr/bin/env python
# -*- coding: utf-8 -*-
# auth : pangguoping
#线程池上下文管理
import contextlib

@contextlib.contextmanager
def worker_state(state_list,worker_thread):
    state_list.append(worker_thread)
    try:
        yield
    finally:
        state_list.remove(worker_thread)

free_list=[]
current_thread = "alex"
with worker_state(free_list,current_thread):
    print(123)
    print(456)