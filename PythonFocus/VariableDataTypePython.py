# _*_ coding : UTF-8_*_
# 开发者 ： zhuozhiwengang
# 开发时间 : 2022/4/28 1:15
# 文件名称 : VariableDataTypePython
# 开发工具 : PyCharm
import keyword
# Python 保留字：Python语言中已经被赋予特殊含义的单词。
print(keyword.kwlist)

# Python 标识符
"""
标识符定义规范：
1、由字母\下划线\_\数字组成，且第一个字符不能是数字
2、不能使用Python 保留字
3、区分字母大小写
"""

# Python 变量
# Python 变量赋值,通过=
num = 5
print("num 变量值:", num)
# Python 是一种动态语言，变量的类型可以随时变化
name = "zhouzhiwengang"
print(type(name))
name = 16
print(type(name))
# Python 内置函数id() 可以用于获取变量存储地址
print(id(name))


# Python 基本数据类型之字符串
# 字符串定义
title = '''珍惜当下,奋勇争先'''
print(title)
# 字符串转义之换行
title = '''珍惜当下,\n奋勇争先'''
print(title)
# 字符串转义之空格
title = '''珍惜当下,\0奋勇争先'''
print(title)
# 字符串转义之双引号
title = '''\"珍惜当下,奋勇争先\"'''
print(title)
