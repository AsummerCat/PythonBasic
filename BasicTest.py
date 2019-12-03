#!/usr/bin/python3
# 单行注释
print("输出语句")

'''
多行注释
1
2
3
'''

"""
上下两个都是多行注释      
"""

# 注意要注意缩进 不然会报错


"""
if判断
"""
if True:
    print("True")
else:
    print("false")
    print("嘿嘿")

"""
多条件判断
"""
a =1
if a==1:
    print("a=1")
elif a==2:
    print("a=2")
else:
    print("a为默认")

"""
多行语句  +\  这个标记
"""
a ="这是一个String类型多行拼接"+\
   "111"+\
    "拼接成功";
print(a)

"""
字符串多行 拼接 : 三个引号
"""
b="""111
1111"""
print(b)

"""
字符串截取 
字符串截取的语法格式如下: 变量[头下标:尾下标:步长]
"""

str="linjingc"
#
print(str) #原字符串
print(str[0:-1]) #输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

"""
等待用户输入
以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。
"""
input("\n\n按下enter键后退出.")

print("end")


a=5;b=3
print(a+b)



'''
Python字符串格式化

'''
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

'''
字符串所看即所得 3引号
'''
a='''
哈哈哈 测试所看即所得
123\n123456
'''
print(a)


'''
f-string 新格式化语句 3.6 -3.8
'''
test='测试哦'
print(f'hello{test}')