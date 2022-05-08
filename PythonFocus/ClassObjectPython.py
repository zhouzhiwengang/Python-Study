# _*_ coding : UTF-8_*_
# 开发者 ： zhuozhiwengang
# 开发时间 : 2022/5/8 16:41
# 文件名称 : ClassObjectPython
# 开发工具 : PyCharm

# 类定义
class Person:
    """
    创建Person 类
    """


# 类实例(对象）
person = Person()
print('类实例存储地址:', person)


# 魔术方法 --init
class Student:
    def __init__(self):
        print("我是魔术方法")


student = Student()


# 对象属性和方法
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def start(self):
        print(self.name, "汽车,售价为:", self.price, '万元')


# 类实例化(对象实例化)
car = Car('奔驰', 135)
# 对象属性
print("我是:", car.name, "汽车")
# 对象方法
car.start()


# 类属性和方法
class Province:
    # 类属性
    country = '中国'

    # 类方法
    @classmethod
    def getCountry(cls):
        print("我来自:", cls.country)


print("Province 类属性访问:", Province.country)
# 类方法调用方式总结
# 方式一:类对象调用类方法
province = Province()
province.getCountry()
# 方式二:类调用类方法
Province.getCountry()


# 计算属性 ：通过@property将方法转换为属性实现
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 计算属性实现
    @property
    def area(self):
        return self.width * self.height


rect = Rect(12, 23)
print('矩形面积为:', rect.area)


# 属性添加安全机制: 通过@property 属性标签，实现私有属性值方法
class User:
    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd

    def getPwd(self):
        return self.__pwd


# User类实例化
user = User('周志刚', '123456')
# 对象直接访问私有属性,提示报错没有发现__pwd 属性
# print("密码是:", user.__pwd)
# 对象访问私有属性的办法,方式一:通过方法返回类实例化对象的私有属性
print("密码是:", user.getPwd())

