"""
    列表list: 存储单一维度的数据 (只存姓名或者年龄).
"""
# 1. 创建: 列表名 = [数据1, 数据2]
list_name = ["夏文剑", "余纯山", "石元峰"]
list_age = [26, 22, 27]
# 列表名 = list(可迭代对象)
list_xwj = list("夏文剑")
print(list_xwj)  # ['夏', '文', '剑']

# 2. 添加
list_name.append("黄涛")  # 追加
list_name.insert(0, "李俊慷")  # 插入
print(list_name)  # ['李俊慷', '夏文剑', '余纯山', '石元峰', '黄涛']

# 3. 定位
# 读取
print(list_name[1])  # 夏文剑
print(list_name[-2:])  # ['石元峰', '黄涛']
# 使用索引或切片修改
list_name[2] = "山山"
list_name[-2:] = ["峰峰", "涛涛"]
print(list_name)  # ['李俊慷', '夏文剑', '山山', '峰峰', '涛涛']

# 4. 删除
# 基于定位: del 容器名[索引或切片]
del list_name[2]
del list_name[-2:]
print(list_name)  # ['李俊慷', '夏文剑']
# 基于元素: 容器名.remove(元素)
list_name.remove("夏文剑")
print(list_name)  # ['李俊慷']

# 5. 遍历
list_num = [26, 22, 27]
# 读取数据: for item in 容器名:
# 打印大于25的年龄
for item in list_num:
    if item > 25:
        print(item)

# 修改数据: for i in range(len(列表名)):
for i in range(len(list_num)):
    if list_num[i] > 25:
        list_num[i] = 25
print(list_num)
