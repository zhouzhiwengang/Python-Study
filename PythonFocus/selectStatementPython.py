# _*_ coding : UTF-8_*_
# 开发者 ： zhuozhiwengang
# 开发时间 : 2022/5/5 0:32
# 文件名称 : selectStatementPython
# 开发工具 : PyCharm

# 选择语句之if
number = int(input("请输入你的年龄:"))
if number == 18:
    print(number, ',合法上网年龄')

# 选择语句之if...else
if number == 18:
    print(number, ',合法上网年龄')
else:
    print(number, ',不适合上网年龄')

# 选择语句之if...elif...else
numberOfProducts = int(input("请输出本月商品销售总数:"))
if numberOfProducts >= 1000:
    print("本月销售任务完成为A")
elif numberOfProducts >=300:
    print("本月销售任务完成为B")
else:
    print("本月销售任务完成为C")

# 选择语句之if 嵌套
if numberOfProducts >= 1000:
    print("本月销售提出为15%")
elif numberOfProducts >=300:
    if numberOfProducts >= 500:
        print("本月销售提出为10%")
    else:
        print("本月销售提出为6%")
else:
    print("本月无销售提出")

# 选择语句之and 条件语句
age = int(input("请输入你的年龄:"))
if age >= 18 and age <= 60:
    print("合法报考驾校年龄")

# 选择语句之 or 条件语句
if age < 18 or age > 60:
    print("非法报考驾校年龄")

# 选择语句之 not 条件语句
encryptNum = int(input("请输入加密数字:"))
encryptList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if encryptNum not in encryptList:
    print('非法输入')