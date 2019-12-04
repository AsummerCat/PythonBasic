'''
自定义函数定义
def
'''


def add(a, b):
    return a + b


print(add(1, 2))

'''
不定长参数 如元组
*参数 表示元组
**参数 表示字典(map)

'''


# 可写函数说明
def printinfo(arg1, *vartuple):
    # "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)


def printinfo(arg1, **vardict):
    #   "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

'''
lambda表达式 
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
'''
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))

'''
将列表当做堆栈  后进先出
'''
stack = [3, 4, 5]
print(stack.pop())
print(stack.pop())
print(stack.pop())

'''
将列表当做队列
'''
from collections import deque

queue = deque(["Eric", "John", "Michael"])
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

'''
列表推导公式
'''
vec = [2, 4, 6]
print([3 * x for x in vec])

'''
同时遍历两个或更多的序列，可以使用 zip() 组合：
'''
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    result1 = 'What is your {0}?  It is {1}.'.format(q, a)
    print(result1)
