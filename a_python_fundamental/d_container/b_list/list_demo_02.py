import copy

list01 = ["北京", ["上海", "深圳"]]
# 赋值: 传递列表地址, 列表只有1份.
list02 = list01
# 浅拷贝: 第一层2份, 深层1份.
list03 = list01[:]
# 深拷贝: 所有层2份.
list04 = copy.deepcopy(list01)

# 深拷贝, 互不影响.
list04[0] = "北京04"
list04[1][1] = "深圳04"
print(list01)  # ['北京', ['上海', '深圳']]

# 浅拷贝, 第一层数据互不影响; 深层数据互相影响.
list03[0] = "北京03"
list03[1][1] = "深圳03"
print(list01)  # ['北京', ['上海', '深圳03']]

# 赋值, 互相影响
list02[0] = "北京02"
list02[1][1] = "深圳02"
print(list01)  # ['北京02', ['上海', '深圳02']]
