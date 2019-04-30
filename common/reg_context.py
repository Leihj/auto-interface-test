# -*- coding: utf-8 -*-
# @File    : re_data.PY
# @Date    : 2019/4/22-11:32
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

#类属性的反射
import re
from common.test_conf import config
from common.test_logging import get_log
import configparser


log = get_log(__name__)
class ConText():
    loan_id=None
    def replace(self,p,data):
        # data='{"mobilephone":"#login_mobile#","pwd":"#login_pwd#"}'
        #原本字符和元字符
        # p='#(.*?)#'    #正则表达式

        #如果要匹配多次，替换多次，使用循环来解决
        while re.search(p,data):
            # print(data)
            m=re.search(p,data)
            g=m.group(1)    #拿到参数化的key
            try:
                v=config.get_str("data",g)  #根据key取配置文件里面的值
            except configparser.NoOptionError as e: #如果配置文件里面没有的时候，去ConText找
                if hasattr(ConText,g):  #判断ConText是否有这个key
                 v = getattr(ConText,g) #有就获取这个key
                else:
                    log.error("找不到参数化的值")   #没有就打印错误日志
                    raise e #抛出异常
            print(v)
            data=re.sub(p,v,data,count=1)   #查找替换，count查找替换的次数

        # if type(data) == str:
        #     data = eval(data)
        return data
# context=ConText()
if __name__ == '__main__':
    res=ConText().replace(p='#(.*?)#',data='{"mobilephone":"#admin_user#","pwd":"#admin_pwd#"}')
    print(res)