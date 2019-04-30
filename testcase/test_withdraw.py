# -*- coding: utf-8 -*-
# @File    : withdraw_testcase.PY
# @Date    : 2019/4/19-17:03
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

import unittest
from common.http_api import Http_Session
from common.test_excel import Do_Excel
from common import contants
from ddt import ddt,data,unpack
from common.reg_context import ConText
from common.test_logging import get_log

log=get_log(__name__)

@ddt
class WithdrawTest(unittest.TestCase):
    excel=Do_Excel(contants.case_data,3)
    cases=excel.create_obj_read_data()

    @classmethod
    def setUpClass(cls):
        log.info("准备测试前置")
        cls.http_request=Http_Session()

    @data(*cases)
    def test_withdraw(self,case):
        log.info("开始执行测试{}".format(case.case_title))  # 打印测试用例title
        case.data=ConText().replace(p='#(.*?)#',data=case.data)
        resp=self.http_request.http_session(case.method,case.url,case.data)
        print(case.method,case.url,case.data)
        actual_code=resp.json()["code"]
        log.debug("actual_code是：{}".format(actual_code))

        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_result(case.case_id+1,resp.text,"PASS")
        except AssertionError as e:
            self.excel.write_result(case.case_id+1,resp.text,"FAILED")
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