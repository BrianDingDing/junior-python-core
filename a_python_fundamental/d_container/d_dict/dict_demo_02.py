"""
    字典推导式
    语法: {键:值 for 变量 in 可迭代对象}
         {键:值 for 变量 in 可迭代对象 if 条件}
"""
# dict_result = {}
# for item in range(10):
#     dict_result[item] = item ** 2
# print(dict_result)
dict_result = {item: item ** 2 for item in range(10)}
print(dict_result)

list_name = ["苏玉", "王陇"]
list_room = [1001, 1002]
# dict_result = {}
# for i in range(len(list_name)):  # 0 1
#     key = list_name[i]
#     value = list_room[i]
#     if value > 1001:
#         dict_result[key] = value
# print(dict_result)
dict_result = {list_name[i]: list_room[i] for i in range(len(list_name)) if list_room[i] > 1001}
print(dict_result)
