# -*- coding: utf-8 -*-
'''
Python3 线程中常用的两个模块为：

_thread
threading(推荐使用)
thread 模块已被废弃。用户可以使用 threading 模块代替。所以，在 Python3 中不能再使用"thread" 模块。为了兼容性，Python3 将 thread 重命名为 "_thread"。
'''

import _thread
import time

'''
語法
_thread.start_new_thread ( function, args[, kwargs] )
'''

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ))
   _thread.start_new_thread( print_time, ("Thread-2", 4, ))
except:
   print ("Error: 无法启动线程")

while 1:
   pass

print("======================================================================================================")
print("======================================================================================================")