# -*- coding: utf-8 -*-
# @File    : test_pymysql.PY
# @Date    : 2019/4/19-14:37
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

import pymysql
from common.test_conf import config

class CommDB():


    # 打开数据库并连接
    def __init__(self):
        self.host=config.get_str("db","host")
        self.user=config.get_str("db","user")
        self.password=config.get_str("db","password")
        self.db=config.get_str("db","db")
        self.port=config.get_int("db","port")
        self.charset=config.get_str("db","charset")
        self.mysql=pymysql.connect(host=self.host,user=self.user,password=self.password,db=self.db,port=self.port,charset=self.charset)

        # self.cursor=self.mysql.cursor()  # 使用cursor()方法获取操作游标
        self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)   #创建游标，以字典格式返回


    #获取查询结果集里面最近的一条数据返回
    def fetch_one(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()


    #获取全部结果集返回
    def fetch_all(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()

    def commit(self):
        return self.mysql.commit()


    #先关闭游标后，再关闭数据库
    def close(self):
        self.cursor.close()
        self.mysql.close()


if __name__ == '__main__':
    db=CommDB()
    res=db.fetch_one("select max(mobilephone) from future.member")
    print(res)

# # 编写sql查询语句，user 对应我的表名
# sql="select * from member where MobilePhone='15154690206'"
#
# try:
#     cur.execute(sql)    #执行sql语句
#     result=cur.fetchall()  #获取查询的所有记录
#     print("ld","MobilePhone")
#     for row in result:
#         id=row[0]
#         regname=row[1]
#         MobilePhone=row[3]
#         print(id,regname,MobilePhone)
# except :
#     print("error")
#
#     db.close()


# import pymysql
#
# db = pymysql.connect(host="test.lemonban.com", user="test", password="test", db="future", port=3306)
#
# cursor=db.cursor()
# cursor.execute("SELECT VERSION()")
# data=cursor.fetchone()
# print("Database version : %s " % data)
# db.close()