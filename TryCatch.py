# -*- coding: utf-8 -*-

'''
异常处理语句
try:

:except:

'''
import sys

while True:
    try:
        x = int(input("请输入一个数字:"))
        break
    except:
        print("您输入的不是数字，请再次尝试输入！")
    finally:
        print("结束输出")

'''
一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如

except (RuntimeError, TypeError, NameError,ValueError):
'''

'''
try/except...else

try/except 语句还有一个可选的 else 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。

else 子句将在 try 子句没有发生任何异常的时候执行。
'''
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

'''
给予异常别名
'''


def this_fails():
    x = 1 / 0
    return x


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

'''
抛出异常
raise [Exception [, args [, traceback]]]
'''
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

'''
抛出异常不处理
'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


