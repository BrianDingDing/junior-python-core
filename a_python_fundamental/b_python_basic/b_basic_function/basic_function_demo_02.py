"""
    print的扩展应用
"""

name = "陈白雪"
age = 26

# 写法1: 输出多个数据. *values带来的便捷.
print("我叫", name, "今年", age, "岁了")

# 写法2: 输出多个数据时, 指定间隔. 使用了命名关键字形参技术.
print("我叫", name, "今年", age, "岁了", sep="")

# 写法3: 多个print函数在一行输出.
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
