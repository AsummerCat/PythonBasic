# -*- coding: utf-8 -*-
# 构建类测试
'''
定义类格式
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
'''


class MyClass:
    """测试实例"""
    i = 123456

    def __init__(self):
        print("MyClass构造函数")

    # 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
    def f(self):
        #  'self表示当前对象'
        print(self.i)
        return 'hello world'


# 实例化类
x = MyClass()
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

print("===================================================================================")
'''
  # 初始化方法 默认ini函数  __init__
'''


class Complex:
    # 初始化方法 默认ini函数  __init__
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5

print("===================================================================================")

'''
私有属性 private 对应 属性名称 __开头 两个下划线开头
私有方法 private 对应 属性名称也是 __开头
'''


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()

print("===================================================================================")

'''
类继承
语法
class DerivedClassName(BaseClassName1):
    <statement-1>
    .
    .
    .
    <statement-N>
'''


class ChildMyClass(MyClass):
    grade = ''

    def __init__(self, g):
        print("ChildMyClass构造函数")
        self.grade = g
        # 覆写父类的方法

    def f(self):
        return "子类方法哦"


x = ChildMyClass("测试")
print(x.f())

print("===================================================================================")

'''
支持
多继承
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
    需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
    方法名同，默认调用的是在括号中排前地父类的方法
'''

print("===================================================================================")

'''
内部作用域无法修改全局变量 给予方法的全是副本 
如果需要修改全局遍历需要使用 global 关键字声明
'''
total = 0  # 这是一个全局变量
num = 999


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)


def test1():
    # 声明修改全局变量
    global num
    print("修改前", num)
    # num = num - 1
    num -= 1
    print("修改后", num)


print("全局变量", num)
test1()
print("全局变量", num)
test1()
print("全局变量", num)
test1()

print("===================================================================================")

'''
嵌套作用域
比如函数内部的函数
如果修改上级作用域的内容 可标记 nonlocal关键字声明 就可以修改了
'''


def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)


outer()

print("===================================================================================")

