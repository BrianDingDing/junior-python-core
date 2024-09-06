list_epidemic = [
    {
        "region": "台湾", "new": 16,
        "now": 2339, "total": 16931,
    },
    {
        "region": "陕西", "new": 182,
        "now": 859, "total": 1573,
    },
    {
        "region": "浙江", "new": 2,
        "now": 505, "total": 2008,
    },
]

# 1. 打印所有疫情信息
for item in list_epidemic:
    print("%s地区新增%s人,现有%s人,累计%s人" % (item["region"], item["new"], item["now"], item["total"]))

# 2. 查找新增人数大于10的地区名称(将结果存入新列表)
list_region = []
for item in list_epidemic:
    if item["new"] > 10:
        list_region.append(item["region"])
        # list_region.append((item["region"], item["total"]))
print(list_region)

# 3. 查找现有人数最大的地区信息(结果为字典)
max_value = list_epidemic[0]
for i in range(1, len(list_epidemic)):
    if max_value["now"] < list_epidemic[i]["now"]:
        max_value = list_epidemic[i]
print(max_value)

# 4. 根据现有人数对疫情信息降序(大->小)排列
for r in range(len(list_epidemic) - 1):
    for c in range(r + 1, len(list_epidemic)):
        if list_epidemic[r]["new"] < list_epidemic[c]["new"]:
            list_epidemic[r], list_epidemic[c] = list_epidemic[c], list_epidemic[r]
print(list_epidemic)
