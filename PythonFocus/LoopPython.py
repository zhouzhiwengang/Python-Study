# _*_ coding : UTF-8_*_
# 开发者 ： zhuozhiwengang
# 开发时间 : 2022/5/5 0:59
# 文件名称 : LoopPython
# 开发工具 : PyCharm

# 循环结构之for
# for 循环之数值循环
for i in(range(1, 50, 5)):
    print("当前数值为:", i)
# for 循环之遍历字符串
str = "珍惜当下, 奋勇争先"
for item in str:
    print("当前字符为:", item)

# 循环结构之while
nums = 1
while nums <= 7:
    print("合法nums值=", nums)
    nums += 1

# 循环结构之break,完全中止循环
for item in str:
    if item == '当':
        print("中止当前for 循环")
        break
    print("当前字符为:", item)
# 循环结构之continue,直接跳到下一次循环
for item in str:
    if item == '当':
        print("直接跳转至当前for 循环的下一个循环")
        continue
    print("当前字符为:", item)