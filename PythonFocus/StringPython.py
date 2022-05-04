# _*_ coding : UTF-8_*_
# 开发者 ： zhuozhiwengang
# 开发时间 : 2022/5/4 23:30
# 文件名称 : StringPython
# 开发工具 : PyCharm

# 字符串操作之拼接
# 温馨提示：字符串的拼接操作通过'+' 实现。
str_start = '珍惜当下,'
str_end = '奋勇当先.'
print(str_start + str_end)

# 字符串操作之计算长度
print(len(str_start + str_end))

# 字符串操作之截取
substr = (str_start + str_end)[:4]
print(substr)

# 字符串操作之检索
# 实现方式一：通过count函数用于检索指定的字符串在字符串中出现的次数。
seachStr = "@马化腾, @马云, @李彦宏, @刘强东"
print('@ 出现次数:', seachStr.count('@'))
# 实现方式二: 通过find 函数用于判别检索的字符串是否在字符串中存在，存在返回出现该字符的首个字符的下标索引，否则返回为-1。
print("马云是否存在:", seachStr.find('马云'))
# 实现方式三：通过index 函数，用法与find 函数一致，不过需要主要的是，如果查找字符串在指定字符串中不存在直接抛出异常
try:
    print("雷军是否存在", seachStr.index('雷军'))
except:
    print('雷军在指定字符串中不存在')
# 实现方式四: 通过startswith 函数判断字符串是否以指定字符串开头
print('字符串是否以@开头', seachStr.startswith('@'))
# 实现方式五: 通过endswith 函数判断字符串是否以指定字符串结尾
print('字符串是否以\'北\'结尾', seachStr.endswith('北'))

# 字符串操作 之大小写转换
# 通过lower 函数实现字符串小写字母转换
letterStr = 'abcdefghijklmnopqrstuvwxyz'
print('字母转小写', letterStr.lower())
# 通过upper 函数实现字符串大写字母转换
print('字母转大写', letterStr.upper())

# 字符串操作之移除空格和特殊字符
str = ' http://www.baidu.com \t\n\r'
# 实现方式一：通过strip 函数去除字符串左右两边的空格和特殊字符
print(str.strip())
# 实现方式二: 通过lstrip 函数去除字符串左边的空格和字符串
print(str.lstrip())
# 实现方式三: 通过rstrip 函数去除字符串右边的空格和字符串
print(str.rstrip())

# 字符串操作之格式化
# 实现方式一：通过'%'操作符
strTemplate = "编号: %09d\t公司名称: %s \t官网: http://www.%s.com"
print(strTemplate%(7, '京东', 'jd'))
# 实现方式二: 通过字符串的format 函数
strTemplate = "编号: {:0>9s}\t公司名称: {:s} \t官网: http://www.{:s}.com"
context = strTemplate.format('7', '京东', 'jd')
print(context)


