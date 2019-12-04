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

''''
repr() 函数可以转义字符串中的特殊字符  repr() 的参数可以是 Python 的任何对象
'''
c = repr("hello\n")
print(c)

'''
这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
'''
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x * x * x).rjust(4))

'''
zfill() 会在数值左边填充0
'''
print('12'.zfill(5))

'''
str.format() 的基本使用如下
'''
print('{}网址： "{}!"'.format('学习使我快乐', 'www.linjingc.top'))
# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('{name}网址： {site}'.format(name='学习使我快乐', site='www.linjingc.top'))
# 位置及关键字参数可以任意的结合:
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))

print('{0:5} ==> {1:10d}'.format(1, 2))

'''
读取键盘输入
'''
str = input("请输入：");
print ("你输入的内容是: ", str)