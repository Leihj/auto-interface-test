import unittest
import json

from ddt import ddt,data,unpack

from common.http_api import Http_Session
from common.test_excel import Do_Excel
from common import contants
from common.reg_context import ConText
from common.test_pymysql import CommDB
from common.test_logging import get_log

log=get_log(__name__)


@ddt
class BidLoanTest(unittest.TestCase):
    excel=Do_Excel(contants.case_data,4)
    cases=excel.create_obj_read_data()


    @classmethod
    def setUpClass(cls):
        log.info("准备测试前置")
        cls.http_request=Http_Session()
        cls.db = CommDB()

    @data(*cases)
    def test_bid_loan(self,case):
        log.info("开始执行测试：{0}".format(case.case_title))
        case.data=ConText().replace(p='#(.*?)#',data=case.data)
        print(case.data)
        data_fill = Do_Excel(contants.case_data, 4)
        resp=self.http_request.http_session(method=case.method, url=case.url, data=case.data)

        log.debug("返回的response是：{}".format(resp))
        actual_code = resp.json()["code"]
        log.debug("actual_code是：{}".format(actual_code))


        try:
            self.assertEqual(str(case.expected),actual_code)
            data_fill.write_result(case.case_id+1,resp.text,"PASS")
            if resp.json()["msg"]=="加标成功":
                sql="SELECT MAX(id) FROM future.loan WHERE memberid=1312  LIMIT 1"
                loan_id=self.db.fetch_one(sql)[0]
                print("loan_id是：",loan_id)
                setattr(ConText,"loan_id",str(loan_id))
        except AssertionError as e:
            data_fill.write_result(case.case_id+1,resp.text,"FAILED")
            log.error("测试报错了：{}".format(e))
            raise e
        log.info("结束测试：{}".format(case.case_title))


    @classmethod
    def tearDownClass(cls):
        log.info("测试后置处理")
        cls.http_request.close()

if __name__ == '__main__':
    unittest.main()
