# _*_ coding : UTF-8_*_
# 开发者 ： zhuozhiwengang
# 开发时间 : 2022/4/28 0:50
# 文件名称 : InOutPython
# 开发工具 : PyCharm

# Python 输出
print("Python 输出")

# Python 输出之ASCII码，通过chr 函数转换输出
print(chr(16))
print(chr(33))

# Python 输出之Python3 采用Unicode字符编码
print("\u4e2d\u56fd")

# Python 输入
tip = input("请输出文字:")
print("用户输入:" + tip)

# 温馨提示:Python3 中, 无论用户输入的是数字还是字符都会被当做字符串处理。

# Python 注释
# 代表单行注释
# '''***''' 或者"""***""" 代表多行注释
"""
短信推送模块
开发者:zhuozhiwengang
版权所有:亚龙辉生物医疗股份公司
"""

# 中文编码注释什么
# 第一种: # -*- coding:utf-8 -*-
# 第二种: # coding=utf-8

# Python 代码缩进
# Python采用代码缩进和冒号: 区分代码之间的层次。

# Python 编码规范
'''
1、每个 import 语句只导入一个模块，尽量避免一次导入多个模块
2、不要在行尾添加分号;
3、建议每行不超过80个字符,如果超过建议使用小括号()将多行内容隐式的连接起来，不推荐使用反斜杠\进行连接
4、增加必要的空行,提升代码可阅读性
5、运算符、函数参数之间和逗号,之间建议使用空格分隔
6、适当使用异常处理，增加程序的健壮性
'''
