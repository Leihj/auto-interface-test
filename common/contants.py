# -*- coding: utf-8 -*-
# @File    : contants.PY
# @Date    : 2019/4/17-15:14
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

import os
# base_dir=os.path.abspath(__file__)      #找到当前文件的绝对路径

# base_dir=os.path.dirname(os.path.abspath(__file__))     #找到当前文件的上一级目录：common

#根目录
base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #找到当前文件的上两级目录：auto_interface根目录


#excel的路径
case_data=os.path.join(base_dir,"test_data","Future_loans.xlsx")   #用base_dir路径与 excel数据文件包名：test_data 与excel数据文件名：Future_loans.xlsx用join做拼接

#conf文件开关项路径
global_file=os.path.join(base_dir,"test_conf","global.conf")    #当前文件的绝对路径拼接test_conf下面的globa.conf配置文件路径,控制环境的开关项

#线上环境路径
online_file=os.path.join(base_dir,"test_conf","on_line.conf")   #当前文件的绝对路径拼接test_conf下面的globa.conf配置文件路径，此环境是正式环境

#测试环境路径
test_file=os.path.join(base_dir,"test_conf","test.conf")    #当前文件的绝对路径拼接test_conf下面的globa.conf配置文件路径，此环境是测试环境

#全部log日志文件夹的路径
all_log=os.path.join(base_dir,"test_report","all_log")  #当前文件的绝对路径拼接test_report下面的log/py15.log配置文件路径，输出日志


#error日志文件夹的路径
error_log=os.path.join(base_dir,"test_report","error_log")


#测试报告的路径
report_html=os.path.join(base_dir,"test_report","html_report")

#测试用例目录的路径
testcase_dir=os.path.join(base_dir,"testcase")

if __name__ == '__main__':

    print(base_dir)
    print(case_data)
    print(global_file)
    print(online_file)
    print(test_file)