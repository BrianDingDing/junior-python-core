"""
    逻辑运算符
        and: 表示并且的关系, 一假俱假. 第一个条件不满足, 第二个条件不执行.
        or: 表示或者的关系, 一真俱真. 第一个条件满足, 第二个条件不执行.
        not: 取反.
    短路逻辑: 提高程序运行效率.
"""
# 有钱 and 有房
# print(int(input("请输入存款: ")) > 100000 and int(input("请输入房产数量: ")) > 0)
# 有钱 or 有房
print(int(input("请输入存款: ")) > 100000 or int(input("请输入房产数量: ")) > 0)
# print(not True)
