# -*- coding: utf-8 -*-
# @File    : add_testcase.PY
# @Date    : 2019/4/25-12:59
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

import unittest
import json

from ddt import ddt,data,unpack

from common.http_api import Http_Session,Do_Excel
from common import contants
from common.reg_context import ConText
from common.test_logging import get_log

log=get_log(__name__)



@ddt
class AddTest(unittest.TestCase):
    excel=Do_Excel(contants.case_data,5)
    cases=excel.create_obj_read_data()

    @classmethod
    def setUpClass(cls):
        log.info("测试前置准备")
        cls.http_request =Http_Session()

    @data(*cases)
    def test_add(self,case):
        log.info("开始执行测试{}".format(case.case_title))  # 打印测试用例title
        case.data = ConText().replace(p='#(.*?)#',data=case.data)
        datafill = Do_Excel(contants.case_data, 5)
        resp=self.http_request.http_session(case.method,case.url,case.data)
        log.debug("返回的response是：{}".format(resp))
        actual_code = resp.json()["code"]
        log.debug("actual_code是：{}".format(actual_code))

        try:
            self.assertEqual(str(case.expected),actual_code)
            datafill.write_result(case.case_id+1,resp.text,"PASS")
        except AssertionError as e:
            datafill.write_result(case.case_id+1,resp.text,"FAILED")
            log.error("测试报错了：{}".format(e))
            raise e
        log.info("结束测试：{}".format(case.case_title))
        # finally:
        #     self.excel.save_excel()


    @classmethod
    def tearDownClass(cls):
        log.info("测试后置处理")
        # cls.excel.close_excel()
        cls.http_request.close()


if __name__ == '__main__':
    unittest.main()
