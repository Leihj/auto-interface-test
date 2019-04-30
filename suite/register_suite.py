# -*- coding: utf-8 -*-
# @File    : register_suite.PY
# @Date    : 2019/4/19-10:27
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

import unittest
from testcase import test_register
from common import contants
import HTMLTestRunnerNew
import time

class RegisterSuite():

     def __init__(self):
         self.suite=unittest.TestSuite()
         self.loader=unittest.TestLoader()

     def add_test_class(self):
         self.suite.addTest(self.loader.loadTestsFromTestCase(test_register.RegisterTest))    #添加测试类
         runner=unittest.TextTestRunner(verbosity=2)
         runner.run(self.suite)


     def add_test_modelu(self):
         self.suite.addTest(self.loader.loadTestsFromModule(test_register))
         # self.write_text()
         self.write_html()


     def write_text(self):
         # self.suite.addTest(self.loader.loadTestsFromModule(register_testcase))

         with open(contants.report_html+"test{}.txt".format(time.strftime('%Y%m%d%H%M%S')),"w",encoding="utf-8") as file:
            runner=unittest.TextTestRunner(stream=file,verbosity=2)
            runner.run(self.suite)

     def write_html(self):
         with open(contants.report_html+"/leihuijuan-test-report{}.html".format(time.strftime('%Y%m%d%H%M%S')),"wb")as file:
             runner = HTMLTestRunnerNew.HTMLTestRunner\
                 (stream=file, title="autointerface测试报告", description="2019年4月19日", tester="leihj")
             runner.run(self.suite)

if __name__ == '__main__':

    RegisterSuite().add_test_modelu()