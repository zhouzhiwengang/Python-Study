# _*_ coding : UTF-8_*_
# 开发者 ： zhuozhiwengang
# 开发时间 : 2022/5/4 11:20
# 文件名称 : ListAndTuplePython
# 开发工具 : PyCharm

# 序列之定义
vars = ['语文', '数学', '英文']
print(vars)
# 序列操作之切片(访问序列指定范围内的元素，通过下标)
print(vars[0:1])
# 序列操作之相加
sciences = ['物理', '化学', '生物', '语文']
print(vars + sciences)
# 温馨提示：序列相加不支持列表和元组相、列表和字符串相加

# 序列操作之乘法
print(sciences * 2)
# 序列操作之判断指定元素是否为序列内的元素
print('语文' in vars)
print('地理' in vars)
# 序列操作之序列长度、序列最大值和序列最小值
nums = [12, 39, 39, 3949, 57, 59, 10, 95, 90]
print('序列长度:', len(nums))
print('序列最大值:', max(nums))
print('序列最小值:',  min(nums))


# 列表操作之创建
# 方式一：使用赋值运算符直接创建列表
teams = ['圣安东尼马刺', '休斯顿火箭', '金州勇士', '洛杉矶湖人']
print(teams)
# 方式二: 创建空列表
emptyList = []
print(emptyList)
#  方式三: 创建数值列表,通过使用list 函数直接将range 函数循环出来的结果转换为列表
numLists = list(range(1, 10, 2))
print(numLists)

# 列表操作之删除列表
del teams

# 列表操作之访问列表中的元素
print(numLists[0])

# 列表操作之遍历列表
# 方式一: 直接使用for 循环遍历实现
for item in numLists:
    print(item)
# 方式二: 使用for 循环 和enumerate() 函数
for index, item in enumerate(numLists):
    print('元素内容:', item, ',所在下标:', index)

# 列表操作之新增、修改和删除列表内的元素
# 添加实现方式一: 通过append 函数实现
numLists.append(119)
print(numLists)
# 添加实现方式二: 通过insert 函数实现，温馨提示：由于insert 添加元素是向指定位置添加，所以执行效率没有append 函数高
numLists.insert(0, 110)
print(numLists)
# 添加实现方式三: 通过extend 函数可以实现将一个列表中的全部元素添加到另一个列表
numLists.extend([110, 112, 119])
print(numLists)

# 修改元素：通过索引获取指定元素，然后再重新为指定元素赋值
print(numLists[0])
numLists[0] = 'Update List'
print(numLists)

# 删除元素实现方式一:根据下标删除
del numLists[0]
# 删除元素实现方式二:根据元素值删除
numLists.remove(119)
print(numLists)

# 列表统计之指定元素出现次数
print('119 出现次数:', numLists.count(119))
# 列表统计之指定元素首次出现的下标位置
print('119 首次出现的下标位置:', numLists.index(119))
# 列表统计之数值列表元素总和
print('总和:', sum(numLists))

# 列表排序
# 列表排序实现方式一:通过列表对象的sort 函数实现
numLists.sort()
print(numLists)
# 列表排序实现方式二: 使用内置函数sorted实现
numLists_desc = sorted(numLists, reverse=True)
print(numLists_desc)

# 元组操作之创建
# 方式一: 使用赋值运算符直接创建元组
numTuple = (1, 2, 3, 10, 11, 4, 5, 5)
print(numTuple)
# 方式二: 创建空元组
emptyTuple = ()
print(emptyTuple)
# 方式三: 使用tuple 函数直接将range函数循环出来的结果转换为数值元组。
rangeTuple = tuple(range(1, 20, 2))
print(rangeTuple)

# 元组操作之删除
del emptyTuple;

# 元组操作之访问元组元素
print(numTuple[0])
print(numTuple[:3])

# 元组操作之修改元组元素
# 温馨提示：元组是不可变序列，所以不能直接对它的单个元素进行修改，但是可以通过对元组进行重新赋值。
numTupleCopy = (1, 2, 3, 10, 11, 4, 5, 5, 9)
numTuple = numTupleCopy
print(numTuple)






