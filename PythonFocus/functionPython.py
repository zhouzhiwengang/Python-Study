# _*_ coding : UTF-8_*_
# 开发者 ： zhuozhiwengang
# 开发时间 : 2022/5/6 1:04
# 文件名称 : functionPython
# 开发工具 : PyCharm

# 函数创建和调用
def fun_bmi(name, height, weight):
    """ 功能：依据身高、体重计算BMI指数
    :param name:
    :param height:
    :param weight:
    :return:
    """
    bmi = weight / (height * height)
    if bmi < 18.5:
        print(name, '的体重偏轻')
    if 18.5 <= bmi < 24.9:
        print(name, '的体重处于正常范围')
    if 24.9 <= bmi < 29.9:
        print(name, '的体重过重')
    if bmi >= 29.9:
        print(name, '的体重处于肥胖')


# 函数调用
fun_bmi("周志刚", 180, 190)


# pass 空语句
def func():
    # pass
    """ 展示pass 空语句
    :return:
    """


# 函数值传递和引用传递
def repeat(obj):
    print("原值：", obj)
    obj += obj


# 值传递
str = "珍惜当下，奋勇争先"
print("函数值传递")
print('函数调用前:', str)
repeat(str)
print('函数调用后:', str)
# 引用传递
lists = ['1', '2', '3']
print("函数引用传递")
print("函数调用前:", lists)
repeat(lists)
print("函数调用后:", lists)


# 可变参数之*parameter
def printTupes(*obj):
    for item in obj:
        print(item)


printTupes('湖南', '广东', '江西', '上海')


# 可变参数之**parameter
def printMap(**obj):
    for key, value in obj.items():
        print('key is：', key, ',value is：', value)


printMap(广东='广州', 湖南='长沙')


# 局部变量
def localVar():
    locaVar = '局部变量'
    print('我是:', locaVar)


localVar()

# 全局变量
globalVar = '全局变量'


def printGlobal():
    print("我是:", globalVar)


printGlobal()

# 匿名函数(lam bal 表达式)
import math

r = 10
result = lambda r: math.pi * r * r
print("半径为：", r, "的，圆面积为：", result(r))
