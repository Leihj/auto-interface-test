# -*- coding: utf-8 -*-
# @File    : main.PY
# @Date    : 2019/5/5-17:13
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com
import sys
sys.path.append('/')
print("sys路径",sys.path)
import HTMLTestRunnerNew
import time
import unittest

from common import contants

dis=unittest.defaultTestLoader.discover(contants.testcase_dir,"test_*.py")

with open(contants.report_html+"/leihuijuan-test-report{}.html".format(time.strftime('%Y%m%d%H%M%S')),"wb+")as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner \
        (stream=file, title="autointerface测试报告", description="2019年4月19日", tester="leihj")
    runner.run(dis)
