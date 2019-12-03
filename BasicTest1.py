'''
end关键字 用于输出一行 后面加上拼接关键字
end=','
'''

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a + b
else:
    print("退出了循环")
