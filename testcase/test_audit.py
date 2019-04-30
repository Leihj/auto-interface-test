# -*- coding: utf-8 -*-
# @File    : audit_testcase.PY
# @Date    : 2019/4/25-13:02
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
class AuditTest(unittest.TestCase):
    excel=Do_Excel(contants.case_data,6)
    cases=excel.create_obj_read_data()


    @classmethod
    def setUpClass(cls):
        log.info("准备测试前置")
        cls.http_request=Http_Session()     #实例化request类

    @data(*cases)
    def test_audit(self,case):
        log.info("开始执行测试{}".format(case.case_title))  # 打印测试用例title
        case.data=ConText().replace(p='#(.*?)#',data=case.data) #用正则表达式，在conf文件替换excel文件的值
        print(case.data)

        datafill = Do_Excel(contants.case_data, 6)
        resp=self.http_request.http_session(method=case.method,url=case.url,data=case.data)
        log.debug("返回的response是：{}".format(resp))
        actual_code = resp.json()["code"]
        log.debug("actual_code是：{}".format(actual_code))
        try:
            self.assertEqual(str(case.expected),actual_code) #case.expected从excel取出来是int类型，要转换成str类型

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