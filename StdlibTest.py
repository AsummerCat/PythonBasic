# -*- coding: utf-8 -*-
# 标准库测试

'''
操作系统接口 os
'''
import datetime
import os

# 操作cmd 命令
# print(os.popen('start.'))

# 返回当前的工作目录
import time

print(os.getcwd())

# 修改当前的工作目录
# os.chdir('/server/accesslogs')

# 执行系统命令 mkdir
# os.system('mkdir today')

# 创建目录
os.mkdir(r"d:\a")

# 返回目录下的所有文件 相当于ls
os.listdir(r"d:\a")

# 删除空的目录
os.rmdir(r"d:\a")

# 递归删除目录和文件
# os.removedirs(path)

# 删除path指向的文件
# os.remove(path)

# 重命名 重命名文件，src和dst为两个路径，分别表示重命名之前和之后的路径。
# os.rename(src, dst)

# 修改权限 相当于chmod
# os.chmod(path, mode)


print("==================================================================")

'''
针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口
shutil则就是对os中文件操作的补充。--移动 复制  打包 压缩 解压，
'''

# 拷贝文件1
# shutil.copyfile('data.db', 'archive.db')

# 重命名
#  shutil.move('/build/executables', 'installdir')

# 仅copy权限，不更改文件内容，组和用户。
# shutil.copymode(src,dst)

# 复制所有的状态信息，包括权限，组，用户，时间等
# shutil.copystat(src,dst)

# 复制文件的内容以及权限，先copyfile后copymode
# shutil.copy(src,dst)

# 复制文件的内容以及文件的所有状态信息。先copyfile后copystat
# shutil.copy2(src,dst)

# 递归的复制文件内容及状态信息
#  shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,ignore_dangling_symlinks=False)

# 递归删除文件
# shutil.rmtree(path, ignore_errors=False, οnerrοr=None)

# 递归移动文件
# shutil.move(src, dst)

# 压缩打包
# base_name：    压缩打包后的文件名或者路径名
# format：          压缩或者打包格式    "zip", "tar", "bztar"or "gztar"
# root_dir :         将哪个目录或者文件打包（也就是源文件）
# shutil.make_archive('tarball','gztar',root_dir='copytree_test')


print("==================================================================")

'''
文件通配符
glob模块提供了一个函数用于从目录通配符搜索中生成文件列表
'''
import glob

# 查询指定目录下的文件  *通配符
print(glob.glob(r'D:\work\pass\src\main\java\com\jeecg\demo\controller\*.java'))

# 查询指定目录下带?的文件  通配符?单个字符
print(glob.glob(r'D:\work\pass\src\main\java\com\jeecg\demo\controller\JeecgDemoExcelControlle?.java'))

# 查询指定目录下 特定字符的范围 通配符
print(glob.glob(r'D:\work\pass\src\main\java\com\jeecg\demo\controller\*[A-Z].java'))

print("==================================================================")

'''
命令行参数
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。例如在命令行中执行 "python demo.py one two three
'''
import sys

print(sys.argv)

# 输出警告
sys.stderr.write('Warning, log file not found starting a new one\n')

'''
sys.version  # 获取Python解释程器的版本信息
sys.maxsize  # 最大的Int值，64位平台是2**63 - 1
sys.path  # 返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
sys.platform  # 返回操作系统平台名称
sys.stdin  # 输入相关
sys.stdout  # 输出相关
sys.stderr  # 错误相关
sys.exc_info()  # 返回异常信息三元元组
sys.getdefaultencoding()  # 获取系统当前编码，默认为utf-8
sys.setdefaultencoding()  # 设置系统的默认编码
sys.getfilesystemencoding()  # 获取文件系统使用编码方式，默认是utf-8
sys.modules  # 以字典的形式返回所有当前Python环境中已经导入的模块
sys.builtin_module_names  # 返回一个列表，包含所有已经编译到Python解释器里的模块的名字
sys.copyright  # 当前Python的版权信息
sys.flags  # 命令行标识状态信息列表。只读。
sys.getrefcount(object)  # 返回对象的引用数量
sys.getrecursionlimit()  # 返回Python最大递归深度，默认1000
sys.getswitchinterval()  # 返回线程切换时间间隔，默认0.005秒
sys.getwindowsversion()  # 返回当前windwos系统的版本信息
sys.hash_info  # 返回Python默认的哈希方法的参数
sys.implementation  # 当前正在运行的Python解释器的具体实现，比如CPython
sys.thread_info  # 当前线程信息
# 程序终止
# sys.exit()
'''

print("==================================================================")

'''
加密包
hashlib 
'''
import hashlib

# 散列加密  最后两个参数 salt 和加密次数 不可逆
dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
dkhex = dk.hex()
print(dk.hex())
dk1 = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
dk1hex = dk1.hex()
print(dk1.hex())
if dk1hex.__eq__(dkhex):
    print("比对成功加密匹配正确")
else:
    print("比对成功加密匹配错误")

print("==================================================================")

'''
字符串正则匹配
import re
'''
import re

# 搜索字符串,以列表类型返回全部能匹配的子串
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

# 在一个字符中替换所有能匹配正则的子串,返回替换的后的字符串  最后一个5表示能替换的最大次数
print(re.sub(r'(\b[a-z]+) \1', r'替换咯', 'cat in the the hat', 5))

print('tea for too'.replace('too', 'two'))

# search 的作用是 查找后面字符中，存在前面字符的情况
m = re.search('[0-9]', "abcd4ef5")
print(m.group(0))

print("==================================================================")

'''
数学函数
math模块
'''
import math

print(math.cos(math.pi / 4))
print(math.log(1024, 2))

print("==================================================================")

'''
随机数
random模块
'''
import random

# 根据数组随机获取一个
print(random.choice(['apple', 'pear', 'banana']))

# 随机获取 指定指定个数
print(random.sample(range(100), 10))

# 返回float
print(random.random())

# 随机获取 限制范围
print(random.randrange(4, 6))
print(random.randrange(6))  # 0-6

print("==================================================================")

'''
访问互联网 http 
'''
# 处理get请求，不传data，则为get请求

import urllib
from urllib.request import urlopen
from urllib.parse import urlencode

url = 'http://www.xxx.com/login'
data = {"username": "admin", "password": 123456}
req_data = urlencode(data)  # 将字典类型的请求数据转变为url编码
res = urlopen(url + '?' + req_data)  # 通过urlopen方法访问拼接好的url
res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)
# 处理post请求,如果传了data，则为post请求

import urllib
from urllib.request import Request
from urllib.parse import urlencode

url = 'http://www.xxx.com/login'
data = {"username": "admin", "password": 123456}
data = urlencode(data)  # 将字典类型的请求数据转变为url编码
data = data.encode('ascii')  # 将url编码类型的请求数据转变为bytes类型
req_data = Request(url, data)  # 将url和请求数据处理为一个Request对象，供urlopen调用
with urlopen(req_data) as res:
    res = res.read().decode()  # read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str

print(res)

print("==================================================================")
'''
发送邮件
import smtplib
'''
# import smtplib
#
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
#                 """To: jcaesar@example.org
#                  From: soothsayer@example.org
#
#                  Beware the Ides of March.
#                 """)
# server.quit()

print("==================================================================")

'''
日期和时间
'''
from datetime import date

now = date.today()
print(now)

# 格式化
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)

# 今天
today = datetime.date.today()
print(today)
# 昨天
yesterday = today - datetime.timedelta(days=1)
print(yesterday)
# 上个月
last_month = today.month - 1 if today.month - 1 else 12
print(last_month)
# 当前时间戳
time_stamp = time.time()
print(time_stamp)
# 时间戳转datetime
print(datetime.datetime.fromtimestamp(time_stamp))
# datetime转时间戳
print(int(time.mktime(today.timetuple())))
# datetime转字符串
today_str = today.strftime("%Y-%m-%d")
print(today_str)
# 字符串转datetime
today = datetime.datetime.strptime(today_str, "%Y-%m-%d")
print(today)
# 补时差
print(today + datetime.timedelta(hours=8))

print("==================================================================")

'''
数据压缩
zlib模块
'''
import zlib

print("==================================================================")

'''
html的转义
'''

import html

# 输出原文
dataHtmlValue = html.escape("<h1>hello world</h1>")
# 转义
html.unescape(dataHtmlValue)

print("==================================================================")
