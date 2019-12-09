# -*- coding: utf-8 -*-
# mysql-connector 测试
# 需要安装提供的驱动  python -m pip install mysql-connector
import mysql.connector

# 连接
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="yourusername",  # 数据库用户名
    passwd="yourpassword"  # 数据库密码
   # ,database="runoob_db" #库名 可指定
)

print(mydb)


# 创建库
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE runoob_db")

# 显示所有库

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


# 创建表

mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")

# 插入数据
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)
mydb.commit()    # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")
print("1 条记录已插入, ID:", mycursor.lastrowid)


# 批量插入
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
]

mycursor.executemany(sql, val)
mydb.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")

# 查询数据
mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)

# 读取指定字段数据
mycursor.execute("SELECT name, url FROM sites")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# 只想读取一条数据，可以使用 fetchone()
mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchone()

print(myresult)


# where 条件语句
sql = "SELECT * FROM sites WHERE name ='RUNOOB'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# 占位符查询
sql = "SELECT * FROM sites WHERE name = %s"
na = ("RUNOOB",)

mycursor.execute(sql, na)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# 删除语句
sql = "DELETE FROM sites WHERE name = 'stackoverflow'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, " 条记录删除")

# 更新语句
sql = "UPDATE sites SET name = %s WHERE name = %s"
val = ("Zhihu", "ZH")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")

# 删除表
sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites

mycursor.execute(sql)