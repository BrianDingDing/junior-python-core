"""
    元组
"""
# 1. 创建
tuple01 = (10, 20)

list01 = ["a", "b", "c"]  # 计算过程中存储数据
tuple02 = tuple(list01)  # 存储计算结果

# 2. 定位
print(tuple02[0])
print(tuple02[:2])

# 3. 遍历
for item in tuple01:
    print(item)

# 注意 1: 在没有歧义的情况下, 元组构建可以省略小括号.
tuple03 = 10, 20, 30
name = "夏文剑",
print(name)

# 注意 2: 元组只有一个元素时, 必须添加逗号.
tuple04 = (10,)

# 注意3: 序列拆包
a, b, c = tuple02  # a,b,c
a, b, c = "夏文剑"  # 夏,文,剑
a, b, c = list01  # a,b,c

# 4. 应用
# 1. 变量交换本质就是创建元组, x, y = y, x; (y, x)是一个元组, 前面是拆包.
x = 1
y = 2
x, y = y, x

# 2. 格式化字符串的本质就是创建元祖:
print("姓名:%s, 年龄:%d" % ("tarena", 15))
