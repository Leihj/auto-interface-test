# -*- coding: utf-8 -*-
# @File    : 111.PY
# @Date    : 2019/4/28-11:34
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

import unittest
import json

from ddt import ddt,data,unpack

from common.http_api import Http_Session
from common.test_excel import Do_Excel
from common import contants
from common.reg_context import ConText

@ddt
class BidLoanTest(unittest.TestCase):
    excel=Do_Excel(contants.case_data,4)
    cases=excel.create_obj_read_data()

    @classmethod
    def setUpClass(cls):
        cls.http_request=Http_Session()

    @data(*cases)
    def test_bid_loan(self,case):

        print("测试标题{}".format(case.case_title))
        case.data=ConText().replace(p='#(.*?)#',data=case.data)
        print(case.data)
        data_fill = Do_Excel(contants.case_data, 4)
        resp=self.http_request.http_session(method=case.method, url=case.url, data=case.data)

        actual_code = resp.json()["code"]


        try:
            self.assertEqual(str(case.expected),actual_code)
            data_fill.write_result(case.case_id+1,resp.text,"PASS")
        except AssertionError as e:
            data_fill.write_result(case.case_id+1,resp.text,"FAILED")
            raise e


    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()

if __name__ == '__main__':
    unittest.main()
