# -*- coding: utf-8 -*-
# @File    : login_suite.PY
# @Date    : 2019/4/19-10:28
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com
import HTMLTestRunnerNew
import time
import unittest

from common import contants
from testcase import test_register
from testcase import test_recharge
from testcase import test_login

# suite=unittest.TestSuite()
# load=loader=unittest.TestLoader()

# suite.addTests(load.loadTestsFromModule(register_testcase))
# suite.addTests(load.loadTestsFromModule(login_testcase))
# suite.addTests(load.loadTestsFromModule(recharge_testcase))

dis=unittest.defaultTestLoader.discover(contants.testcase_dir,"test_*.py")

with open(contants.report_html+"/leihuijuan-test-report{}.html".format(time.strftime('%Y%m%d%H%M%S')),"wb+")as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner \
        (stream=file, title="autointerface测试报告", description="2019年4月19日", tester="leihj")
    runner.run(dis)
