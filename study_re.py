# -*- coding:utf-8 -*-
# @Project: auto_interface 
# File: study_re
# Author: leihuijuan
# Date: 2019/4/22-0:31
# Email: huijuan_lei@163.com
import re
from common.test_conf import config

data='{"mobilephone":"#login_mobile#","pwd":"#login_pwd#"}'
# 原本字符和元字符
p='#(.*?)#'    #正则表达式

m=re.search(p,data) #任意位置开始找，找到第一个就返回
print(m.group(0))   #返回表达式和组里面的内容
x=(m.group(1))   #返回指定组的内容
v=config.get_str("data",x)
print(v)
ms=re.findall(p,data)   #查找全部，返回列表
# print(ms)
