# -*- coding: utf-8 -*-
# @File    : http_api.PY
# @Date    : 2019/4/15-17:44
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

#方法一：利用登录接口返回的cookies值，作为充值接口中请求的cookies值
import requests
import json
from common.test_excel import Do_Excel
from common.test_conf import config
from common.test_logging import get_log

log=get_log(__name__)

class Http_Request():

    def http_request(self,method,url,data=None,json=None,cookies=None):
        method=method.lower()
        url=config.get_str("api","url")+url #配置文件路径和excel的url地址拼接成请求的url地址

        if type(data)==str:
            data=eval(data)

        if method =="get":
           resp=requests.get(url,params=data,cookies=cookies)


        elif method=="post":
            if data:
                resp=requests.post(url,data=data,cookies=cookies)
            else:
                resp=requests.post(url,json=json,cookies=cookies)
        else:
            resp=print("not this method")
        log.debug("请求的url是:", url)
        log.debug("请求的response：", resp.text)
        return resp


#方法二：利用session传值，充值方法中不用参数化cookies了
class Http_Session():
    def __init__(self):
        self.session=requests.session()

    def http_session(self,method,url,data=None,json=None):
        method=method.upper()
        url=config.get_str("api","url")+url #配置文件路径和excel的url地址拼接成请求的url地址
        print(url)

        if type(data)==str:
            data=eval(data)

        if method=="GET":
            resp=self.session.request(method=method,url=url,params=data)

        elif method=="POST":
            if data :
                resp=self.session.request(method=method,url=url,data=data)
            else:
                resp=self.session.request(method=method,url=url,json=json)
        else:
            resp=None
            log.error("nonsupport method")
        log.debug("请求的url是: {}".format(url))
        log.debug("请求的response：{}".format(resp.text))

        return resp

    def close(self):
        self.session.close()


if __name__ == '__main__':


    from common import contants
    #   #contants.case_data  获取 Future_loans.xlsx的绝对路径
    # excel = Do_Excel(contants.case_data, 1)
    # res = excel.create_obj_read_data()
    # for i in res:
    #     print(i.case_id)
    #     print(i.case_title)
    #     print(i.url)
    #     print(i.__dict__)













    # res=Http_Request().http_request("POST","http://test.lemonban.com/futureloan/mvc/api/member/login",data={"mobilephone":"15810447878","pwd":"123456"})
    # print(res.cookies)
    # res=Http_Request().http_request("post","http://test.lemonban.com/futureloan/mvc/api/member/recharge",data={"mobilephone":"15810447878","amount":"123456"},cookies=res.cookies)
    # print(res.text)
    #
    # session=requests.session()
    #
    api=Http_Session()
    data = {"mobilephone": "13187250598", "pwd": "123456"}
    resp=api.http_session("post",url="/member/login",data=data)
    # resp=session.request("post",url="http://test.lemonban.com/futureloan/mvc/api/member/login",data=data)

    print(resp.status_code)
    print(resp.text)
    print(resp.cookies)

    data = {"memberId":1062,"title":"投资超市","amount":10000,"loanRate":18.0,"loanTerm":30,"loanDateType":0,"repaymemtWay":11,"biddingDays":9}
    resp = api.http_session("post", url="/loan/add", data=data)
    # data = {"mobilephone": "15810447878", "amount": "123456"}
    # resp=session.request("post",url="http://test.lemonban.com/futureloan/mvc/api/member/recharge",data=data)
    print(resp.status_code)
    print(resp.text)
    print(resp.cookies)


    #自动传cookies值的用法
    # api=Http_Session()      #实例化一个对象，id不一致，sessionID也不一致
    #
    # resp=api.http_session("POST","http://test.lemonban.com/futureloan/mvc/api/member/login",data={"mobilephone":"15810447878","pwd":"123456"})
    # print(id(Http_Session()))
    # print(resp.status_code)
    # print(resp.text)
    # print(resp.cookies)
    #
    # resp=api.http_session("post","http://test.lemonban.com/futureloan/mvc/api/member/recharge",data={"mobilephone":"15810447878","amount":"123456"})
    # print(id(Http_Session()))
    # print(resp.status_code)
    # print(resp.text)
    # print(resp.cookies)

