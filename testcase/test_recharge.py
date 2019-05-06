# -*- coding: utf-8 -*-
# @File    : recharge.PY
# @Date    : 2019/4/15-17:41
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

import unittest

from common.test_excel import Do_Excel
from common import contants
from  common.http_api import Http_Session
from ddt import ddt,data,unpack
from common.reg_context import ConText
from common.test_logging import get_log
from common.test_pymysql import CommDB


log=get_log(__name__)

@ddt
class RechargeTest(unittest.TestCase):

    excel=Do_Excel(contants.case_data,2)
    cases=excel.create_obj_read_data()


    @classmethod
    def setUpClass(cls):
        log.info("测试前置准备")
        cls.http_request=Http_Session()
        cls.db=CommDB()

    @data(*cases)
    def test_recharge(self,case):
        if case.sql is not None:
            sql = eval(case.sql)['sql1']  # 取到excel的check_sql列的第一条sql语句
            amount = self.db.fetch_one(sql)  # 执行sql语
            # 句
            print("金额",amount['LeaveAmount'])
            before_amount = amount['LeaveAmount']  # 充值之前的金额

        case.data = ConText().replace(p='#(.*?)#', data=case.data)  # 加入正则表达式
        resp=self.http_request.http_session(case.method,case.url,case.data)
        actual_code=resp.json()["code"] #返回的code

        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_result(case.case_id+1,actual_code,"PASS")
            if case.sql is not None:
                sql = eval(case.sql)['sql1']  # 取到excel的check_sql列的第一条sql语句
                amount = self.db.fetch_one(sql)  # 执行sql语句
                after_amount = amount['LeaveAmount']
                recharge_amount=float(eval(case.data)['amount'])
                self.assertEqual(float(before_amount)+recharge_amount,float(after_amount))    #充值之前的金额+这次充值的金额 与 充值之后的金额做对比
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,actual_code,"FAILED")
            log.error("出错了：{}".format(e))
            raise e
        log.info("测试结束了{}".format(case.case_title))

    @classmethod
    def tearDownClass(cls):
        log.info("测试后置处理")
        cls.http_request.close()   #关闭请求
        cls.db.close()


if __name__ == '__main__':
    unittest.main()