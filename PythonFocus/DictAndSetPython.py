# _*_ coding : UTF-8_*_
# 开发者 ： zhuozhiwengang
# 开发时间 : 2022/5/6 0:07
# 文件名称 : DictAndSetPython
# 开发工具 : PyCharm

# 字典操作之创建
# 实现方式一:字典定义
dictionary = {'name': '周志刚', 'age': 30, 'address': '广东深圳市'}
print(dictionary)
# 基于dict函数,实现方式二: 通过映射函数创建字典
cityDict = dict(zip(['广东省', '湖南省', '江西省', '上海市', '山西省'], ['广州', '长沙', '南昌', '上海', '太原']))
print(cityDict)
# 基于Dicth函数,实现方式三: 通过给定'键值对',创建字典
scoreDict = dict(A=100, B=80, C=60, D='不合格')
print(scoreDict)
# 基于dict.fromkeys()方法创建值为空的字典,实现方式四
teamDict = dict.fromkeys(['火箭队', '湖人队', '勇士队', '掘金队'])
print(teamDict)

# 字典操作之访问
# 通过键值实现字典访问
print(teamDict['火箭队'])
# 温馨提示: 如果访问的键值在字典中，不存在会抛出异常
try:
    print(teamDict['凯尔特人'])
except:
    print("凯尔特人在指定字典中无法找到")

# 通过字典对象的get()方法，或者指定的值
print(teamDict.get('火箭队', '火箭队在指定字典中无法找到'))

# 字典操作之遍历
# 字典遍历通过字典对象的items()方法,可以获取字典中的'键值队'列表
for item in teamDict.items():
    print(item)
# 字典遍历通过字典对象的items()方法,可以获取字典中的'键值队'
for key, value in teamDict.items():
    print('字典key:', key, ',字典value:', value)

# 字典操作之新增、修改和删除
# 字典操作之新增
teamDict['森林狼'] = None
print(teamDict)
# 字典操作之修改,添加一个元素，当元素存在时，则相当于修改功能
teamDict['森林狼'] = '狼王'
print(teamDict)
# 字典操作之删除
del teamDict['森林狼']
print(teamDict)


# 集合操作之创建
# 实现方式一:直接使用'{}',进行创建
setObject = {'东北', '华北', '华东', '华中', '华南', '西南', '西北'}
print(setObject)
# 实现方式二:使用set()函数将列表、元组等可迭代对象转换为集合
print(set([1, 2, 3, 4]))

# 集合操作之添加元素
setObject.add('中')
print(setObject)
# 集合操作之移除元素
setObject.remove('中')
print(setObject)

# 集合之交集、并集和差集
teamOne = set(['姚明', '麦迪', '加内特'])
teamTwo = set(['邓肯', '姚明', '奥尼尔'])
print("交集运算:", teamOne & teamTwo)
print("并集运算:", teamOne | teamTwo)
print("差集运算:", teamOne - teamTwo)
