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


log=get_log(__name__)

@ddt
class RechargeTest(unittest.TestCase):

    excel=Do_Excel(contants.case_data,2)
    cases=excel.create_obj_read_data()

    @classmethod
    def setUpClass(cls):
        log.info("测试前置准备")
        cls.http_request=Http_Session()

    @data(*cases)
    def test_recharge(self,case):
        log.info("开始执行测试{}".format(case.case_title))   #打印测试用例title
        case.data=ConText().replace(p='#(.*?)#',data=case.data)   #加入正则表达式
        datafill = Do_Excel(contants.case_data, 2)

        resp=self.http_request.http_session(case.method,case.url,case.data)
        log.debug("返回的response是：{}".format(resp))
        actual_code=resp.json()["code"] #返回的code

        try:
            self.assertEqual(str(case.expected),actual_code)
            datafill.write_result(case.case_id+1,actual_code,"PASS")
        except AssertionError as e:
            self.datafill.write_result(case.case_id+1,actual_code,"FAILED")
            log.error("出错了：{}".format(e))
            raise e
        # finally:
            # self.excel.save_excel() #保存excel
        log.info("测试结束了{}".format(case.case_title))

    @classmethod
    def tearDownClass(cls):
        log.info("测试后置处理")
        # cls.excel.close_excel()     #关闭excel
        cls.http_request.close()   #关闭请求


if __name__ == '__main__':
    unittest.main()