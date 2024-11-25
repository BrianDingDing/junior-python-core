"""
    字典存储多个维度数据
"""

# 1.创建
dict_ycs = {
    "name": "余纯山",
    "age": 22,
    "sex": "男",
}
dict_th = {
    "name": "覃航",
    "age": 26,
    "sex": "女",
}

# 列表转为字典, 列表中的元素必须能够一分为二.
print(dict([("name", "覃航"), ("age", 26)]))  # {'name': '覃航', 'age': 26}

# 2. 添加 / 定位 / 读取
#  字典名[键] = 值
dict_ycs["money"] = 1000000  # 添加
dict_ycs["sex"] = "女"  # 修改
print(dict_ycs["name"])  # 读取, 余纯山, 没有key会报错

# 3. 删除
del dict_ycs["sex"]
print(dict_ycs)  # {'name': '余纯山', 'age': 22, 'money': 1000000}

# 4. 遍历
for key in dict_th:
    print(key)

for value in dict_th.values():
    print(value)

# for item in dict_th.items():  # item: ('name', '余纯山'), 是个元组.
#     print(item)
for key, value in dict_th.items():  # 拆包
    print(key)
    print(value)

# 5. dict -> list
print(list(dict_th))  # ['name', 'age', 'sex']
print(list(dict_th.values()))  # ['覃航', 26, '女']
print(list(dict_th.items()))  # [('name', '覃航'), ('age', 26), ('sex', '女')]
