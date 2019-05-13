# -*- coding: utf-8 -*-
# @File    : test_conf.PY
# @Date    : 2019/4/16-18:16
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

from configparser import ConfigParser
from common import contants

class Read_Conf():
    def __init__(self):
        self.conf=ConfigParser() #实例化
        self.conf.read(contants.global_file,encoding="UTF-8")       #获取到global的绝对路径
        switch=self.conf.getboolean("switch","on_off")  #获取到global配置文件switch区块下on_off对应的value值
        if switch:  #开关打开的时候，使用on_line的配置
            self.conf.read(contants.online_file,encoding="UTF-8")
        else:   #开关关闭的时候，使用test的配置

            self.conf.read(contants.test_file,encoding="UTF-8")

    #获取所有的sections，区块名
    def get_sections(self):
        return self.conf.sections()

    #获取某个区块下面所有的options，包括key和value
    def get_options(self,section):
        return self.conf.options(section)

    #获取某个options对应的value值，返回的是字符串
    def get_str(self,section, option):
        return self.conf.get(section, option)

    # 获取某个options对应的value值，返回的是字符串，把字符串转换成int型
    def get_int(self,section,option):
        return self.conf.getint(section,option)

    # 获取某个options对应的value值，返回的是字符串，把字符串转换成float型
    def get_float(self,section,option):
        return self.conf.getfloat(section,option)

    # 获取某个options对应的value值，返回的是字符串，把字符串转换成布尔型(Ture和False)
    def get_boolean(self,section,option):
        return self.conf.getboolean(section,option)

    # 获取某个options对应的value值，返回的是字符串，把字符串转换成python所认识的字符类型
    def get_eval(self,section,option):
        return eval(self.conf.get(section,option))

config = Read_Conf()  # 将Read_Conf这个类实例化

if __name__ == '__main__':

   print(config.get_str("api","url"))
   print(config.get_sections())
