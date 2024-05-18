"""
    内置生成器函数: zip
"""
list_name = ["aa", "bb", "cc"]
list_room = [1001, 1002, 1003]

for item in zip(list_name, list_room):
    print(item)

# 矩阵转置
map = [
    [2, 0, 2, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]

new_map = []
# for item in zip(map[0], map[1], map[2], map[3]):
for item in zip(*map):  # 拆
    new_map.append(list(item))
print(new_map)

new_map = [list(item) for item in zip(*map)]
print(new_map)

# 练习: 将两个列表合成为一个字典
list_student_name = ["悟空", "八戒", "白骨精"]
list_student_age = [28, 25, 36]

dict_result1 = {}
for item in zip(list_student_name, list_student_age):
    dict_result1[item[0]] = item[1]

print(dict_result1)

dict_result2 = {item[0]: item[1] for item in zip(list_student_name, list_student_age)}
print(dict_result2)

# 可迭代对象转换为以下容器: list, dict, tuple. 内部都具有__next__函数循环调用. 因此dict能转换zip.
dict_result3 = dict(zip(list_student_name, list_student_age))
print(dict_result3)
