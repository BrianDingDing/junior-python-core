"""
    生成器表达式: 相比列表推导式, 更节省内存
"""
list01 = [43, 54, 5, 345, 34, 65, 3]

# list_new = [item ** 2 for item in list01]
generator_new = (item ** 2 for item in list01)

for item in generator_new:
    print(item)
