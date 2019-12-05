# -*- coding: utf-8 -*-
# ##以utf-8编码储存中文字符

# 文件输出输入
'''

open() 将会返回一个 file 对象，基本语法格式如下:
open(filename, mode)
ilename：包含了你要访问的文件名称的字符串值。
mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
不同模式打开文件的完全列表：
https://www.runoob.com/python3/python3-inputoutput.html
'''

# 需要导入模块
import codecs


# 写入文件
f = codecs.open("D:/pythonDdemo/basic/fileTest.txt", "w+", encoding='utf-8')
wText = "输出语句转换UTF-8\n"
f.write(wText)
f.writelines("下一行\n")
f.writelines("下一行")
f.close()

# 读取文件 read()
f = codecs.open("D:/pythonDdemo/basic/fileTest.txt","r",encoding='utf-8')
 ## 一次性读取
str=f.read()
print(str)
f.close()

# 读取文件 读取单行 f.readline() 换行符为 '\n   readline() 如果返回一个空字符串, 说明已经已经读取到最后一行
f = codecs.open("D:/pythonDdemo/basic/fileTest.txt","r",encoding='utf-8')
 ## 一次性读取
str=f.readline()
print(str)
f.close()

# f.readlines() 将返回该文件中包含的所有行。
f = codecs.open("D:/pythonDdemo/basic/fileTest.txt","r",encoding='utf-8')
str=f.readlines()
print(str)
f.close()

# 遍历
f = codecs.open("D:/pythonDdemo/basic/fileTest.txt","r",encoding='utf-8')
for line in f:
    print(line, end='')
f.close()

# 写入返回写入的字符数
f = codecs.open("D:/pythonDdemo/basic/fileTest.txt","w",encoding='utf-8')
num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
# 关闭打开的文件
f.close()


import os

print(os.path)
print(os.pipe())
# 获取当前目录下的文件列表
print(os.listdir("D:/pythonDdemo/basic"))
