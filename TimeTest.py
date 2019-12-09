# -*- coding: utf-8 -*-
import time;  # 引入time模块

ticks = time.time()
print ("当前时间戳为:", ticks)


# 获取当前时间
#从返回浮点数的时间戳方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

# 获取格式化的时间
localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

'''
格式化时间
time.strftime(format[, t])
'''
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

print("====================================================================")
print("====================================================================")

'''
Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
'''
# 获取某月日历
import calendar

cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)