# -*- coding: utf-8 -*-
# @File    : register_testcase.PY
# @Date    : 2019/4/15-17:40
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

import unittest
from common import http_api
from common.test_excel import Do_Excel
from common import contants
from ddt import ddt,data,unpack
from common.test_pymysql import CommDB
from common.test_logging import get_log

log=get_log(__name__)

@ddt
class RegisterTest(unittest.TestCase):
    excel=Do_Excel(contants.case_data,0)
    cases=excel.create_obj_read_data()

    @classmethod
    def setUpClass(cls):
        log.info("测试前置准备")
        cls.http_request=http_api.Http_Session()    #实例化request的session类
        cls.commdb=CommDB() #实例化mysql类

    @data(*cases)
    def test_register(self,case):
        log.info("开始执行测试{}".format(case.case_title))

        if case.data.find("normal_user") >-1:
            # sql="SELECT max(mobilephone) FROM future.member WHERE mobilephone LIKE '1860735%'"
            sql=case.sql  #执行excel里面的sql语句
            # sql="select max(mobilephone) from future.member"
            max_phone=self.commdb.fetch_one(sql)[0]
            # print("mysql:",max_phone)#查询最大手机号码，返回的是元组，根据索引获取第一条数据
            before_max_phone=int(max_phone)+1#max_phone是str类型，转成int类型，最大手机号码+1（也可以最小手机号码-1）
            log.debug("before_max_phone号码:{}".format(before_max_phone))

            #字符串的替换
            case.data=case.data.replace("normal_user",str(before_max_phone))
            self.commdb.commit()  # 修改或替换数据后，mysql要提交，否则后面有参数的数据将不会执行

        datafill = Do_Excel(contants.case_data, 0)  #再次打开excel读取数据
        resp = self.http_request.http_session(case.method, case.url, case.data)
        log.debug("返回的response是：{}".format(resp))

        try:
            self.assertEqual(str(case.expected),resp.text)
            datafill.write_result(case.case_id+1,resp.text,"PASS")

            # 判断注册成功之后，查询数据库，取到mobilephone
            if resp.json()['msg']=="注册成功":
                # sql = "select max(mobilephone) from future.member where mobilephone like '1860735%'"
                sql = case.sql    #执行excel里面的sql语句
                log.debug("执行的sql语句是：{}".format(sql))
                after_max_phone = self.commdb.fetch_one(sql)[0]
                # print("mysql:", after_max_phone)  # 查询最大手机号码，返回的是元组，根据索引获取第一条数据
                log.debug("注册成功后的最大号码：{}".format( after_max_phone))

                self.assertEqual(str(before_max_phone),after_max_phone)
        except AssertionError as e:
            datafill.write_result(case.case_id+1,resp.text,"FAILED")
            log.error("出错了：{}".format(e))
            raise e

        self.commdb.commit()  # 修改或替换数据后，mysql要提交，否则后面有参数的数据将不会执行
        log.info("测试结束了{}".format(case.case_title))


    @classmethod
    def tearDownClass(cls):
        log.info("测试后置处理")
        # cls.excel.close_excel()
        cls.commdb.close()


if __name__ == '__main__':
    unittest.main()