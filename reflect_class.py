# -*- coding: utf-8 -*-
# @File    : reflect_class.PY
# @Date    : 2019/4/24-10:27
# @Author  : leihuijuan
# @Emali    : huijuan_lei@163.com

class Reflect():
    eyes=2

    def __init__(self,name,hobby):
        self.name=name
        self.hobby=hobby


if __name__ == '__main__':

    pople=Reflect("mogon","python")
    print(Reflect.eyes)
    print(pople.eyes)
    print(pople.name)

    #查看是否有name属性
    print(hasattr(pople,"eyes"))    #如果有返回True
    print(hasattr(pople,"sex"))     #如果没有返回False


    #添加属性，如果没有该属性则添加，如果有该属性，则覆盖属性的value值
    setattr(Reflect,"age",27)   #设置类属性：类名，属性名， 属性值
    print(hasattr(Reflect,"age"))   #
    print(Reflect.age)


    setattr(pople,"dance",True) #设置实例属性  实例化名，属性名，属性值
    print(pople.dance)