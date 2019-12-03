# 标准数据类型
"""
Python3 中有六个标准的数据类型：

Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：

不可变数据（3 个）：Number（数字）、String（字符串）、Tuple格式:()（元组）；
可变数据（3 个）：List格式:[]（列表）、Dictionary（字典）、Set格式:{}（集合）。
"""

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']
# 新增
list.append("cc")
print(list)
# 删除
list.remove(786)
print(list)
# 拼接
print(list + tinylist)

# 反转
list.reverse()
print(list)

# 改变元素
list[0] = 9
print(list)
list[2:5] = [13, 14, 15]
print(list)

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

print("===========================================================")

# 元组=数组
"""
元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
"""
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

print("===========================================================")

# 集合 自动去重
"""
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

创建格式：

parame = {value01,value02,...}
或者
set(value)
"""
parame = set()
# or
parame = {}

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素
print("===========================================================")

# java的hashMap=Dictionary（字典）
"""
字典（dictionary）是Python中另一个非常有用的内置数据类型。

列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。

键(key)必须使用不可变类型。

在同一个字典中，键(key)必须是唯一的。
"""
dict = {}
dict['1'] = "1-第一个value"
dict['2'] = "第二个value"
for key in dict.keys():
    print(key + ':' + dict[key])

# 方式一：
for key in dict:
    print(key + ':' + dict[key])
# 方式二：
for key in dict.keys():
    print(key + ':' + dict[key])
# 方式三：
for key, value in dict.items():
    print(key + ':' + value)
# 方式四：
for (key, value) in dict.items():
    print(key + ':' + value)

# 遍历字典项
for kv in dict.items():
    print(kv)