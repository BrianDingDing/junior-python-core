"""
    在python中变量没有类型, 但关联的对象有类型.
"""
# 1. 字符串str: 存储文本, 使用双引号修饰.
name = "杨帅"

# 2. 整型int: 存储整数, 直接写数字.
age = 26

# 3. 浮点型float: 存储小数, 带上小数点.
score = 96.8

print("100" + "1")  # 文本拼接
print(100 + 1)  # 数学计算
# print("100" + 1) # python语言不支持字符串与数值类型运算

# input函数的结果一定是字符串类型
age = int(input("请输入您的年龄: "))
print("明年您就" + str(age + 1) + "岁了")

# 4. 类型转换: 结果 = 目标类型(等转数据)
# str <-> int
data01 = int("8")
data02 = str(8)

# str <-> float
data03 = float("1.8")
data04 = str(1.8)

# int <-> float
data05 = float(8)
data06 = int(7.99)  # 截断删除
print(data06)  # 7

# 当字符串类型转换为其他类型时, "长得必须像"目标类型, 否则报错.
# int("250.6")
