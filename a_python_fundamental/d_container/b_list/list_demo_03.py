"""
    list -> str
"""
list01 = ["a", "b", "c"]
result = "-".join(list01)
print(result)  # a-b-c

# 面试题: 根据条件, 循环拼接字符串
# str_result = ""
# for item in range(10):
#     # 字符串不可变, 每次循环都会创建新字符串, 成为垃圾.
#     # 0
#     # 01
#     # 012
#     # 0123...
#     str_result += str(item)
# print(str_result)

# 解决: 使用列表代替字符串
list_result = []
for item in range(10):
    # 每次向同一个列表添加, 所以没有垃圾.
    list_result.append(str(item))
result = "".join(list_result)
print(result)

"""
    str --> list
"""
# 使用一个字符串存储多个信息
list_result = "唐僧,孙悟空,八戒".split(",")
print(list_result)
