"""
    列表推导式: 根据可迭代对象, 以简易的方式构建新列表.
    语法:
        变量 = [表达式 for 变量 in 可迭代对象]
        变量 = [表达式 for 变量 in 可迭代对象 if 条件]
"""

# 生成10 - 30之间能被3或者5整除的数字
# list_result = []
# for item in range(10,31):
#     if item % 3 ==0 or item % 5 ==0:
#         list_result.append(item)
# print(list_result)
list_result = [item for item in range(10, 31) if item % 3 == 0 or item % 5 == 0]
print(list_result)

# 生成5 - 20之间的数字平方
# list_result = []
# for item in range(5,21):
#     list_result.append(item ** 2)
# print(list_result)
list_result = [item ** 2 for item in range(5, 21)]
print(list_result)
