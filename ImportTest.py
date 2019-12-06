# 导包操作测试
"""
在 python 用 import 或者 from...import 来导入相应的模块。

将整个模块(somemodule)导入，格式为： import somemodule

从某个模块中导入某个函数,格式为： from somemodule import somefunction

从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

将某个模块中的全部函数导入，格式为： from somemodule import *
"""
import sys

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

from sys import path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

'''
调用其他模块
'''
import function

# from function import add 指定函数调用

print(function.add(1, 2))

'''
如果在当前页常用还可以将函数赋值给var
'''
addTest = function.add
print(addTest(1, 2))

'''
__name__属性 来判断是否在当前模块运行
'''
if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')

'''
dir()  内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回
'''
print(dir(sys))
'''
dir() 不给参数能获取到当前模块的参数
'''
a=5
print(dir())
del a
print(dir())