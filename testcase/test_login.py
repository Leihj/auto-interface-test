# -*- coding: utf-8 -*-
# @File    : login_testcase.PY
# @Date    : 2019/4/15-17:41
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

import unittest
from common.http_api import Http_Session
from common.test_excel import Do_Excel
from ddt import ddt,data,unpack
from common import contants
from common.reg_context import ConText
from common.test_logging import get_log


log=get_log(__name__)

@ddt
class LoginTest(unittest.TestCase):
    excel=Do_Excel(contants.case_data,1)
    cases=excel.create_obj_read_data()


    #setUpClass(): 必须使用 @ classmethod装饰器, 所有case运行之前只运行一次

    @classmethod
    def setUpClass(cls):
        log.info("测试前置准备")
        cls.http_request=Http_Session()

    @data(*cases)
    def test_login(self,case):
        log.info("开始执行测试{}".format(case.case_title))

        #数据读取方法一：
        # case.data=eval(case.data)
        # print(case.data)
        #
        # #判断case.data里面是否有mobilephone这个key，且key的值是否等于login_mobile
        # if case.data.__contains__("mobilephone") and case.data["mobilephone"]=="login_mobile":
        #     #如果有，则case.data["mobilephone"]替换成配置文件ogin_mobile的value值
        #     case.data["mobilephone"]=config.get_str("data","login_mobile")
        #
        # #判断case.data里面是否有mobilephone这个key，且key的值是否等于login_mobile
        # if case.data.__contains__("pwd") and case.data["pwd"]=="login_pwd":
        #     # 如果有，则case.data["mobilephone"]替换成配置文件ogin_mobile的value值
        #     case.data["pwd"]=config.get_str("data","login_pwd")

        #数据读取方法二：
        #正则表达式
        case.data=ConText().replace(p='#(.*?)#',data=case.data)
        print(type(case.data))
        datafill = Do_Excel(contants.case_data,1)
        resp=self.http_request.http_session(case.method,case.url,case.data)
        # actual_code=resp.json()["code"] #获取实际结果的code
        log.debug("返回的response是：{}".format(resp))
        try:
            self.assertEqual(str(case.expected),resp.text)   #预期结果和时间结果对比
            datafill.write_result(case.case_id+1,resp.text,"PASS")    #写入实际结果，和通过结果：pass
        except AssertionError as e:
            datafill.write_result(case.case_id+1,resp.text,"FAILED")   #写入实际结果，和通过结果：failed
            log.error("出错了：{}".format(e))
            raise e #抛出异常
        log.info("测试结束了{}".format(case.case_title))

    #tearDownClass(): 必须使用 @ classmethod装饰器, 所有case运行完之后只运行一次
    @classmethod
    def tearDownClass(cls):
        # cls.excel.save_excel()
        # cls.excel.close_excel()
        log.info("测试后置处理")
        cls.http_request.close()



if __name__ == '__main__':
   unittest.main()