# python 迭代 iter

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
print(next(it))  # 输出迭代器的下一个元素
print(next(it))

'''
 迭代器遍历普通遍历
'''
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
for x in list:
    print(x)

'''
使用next 获取下一个值 进行遍历
'''
import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
