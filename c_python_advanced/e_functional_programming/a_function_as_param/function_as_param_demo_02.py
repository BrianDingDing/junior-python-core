"""
    函数式编程思想
        适用性: 多个函数主体结构相同, 核心算法不同
        分: 将变化点单独定义在函数中
        隔: 使用参数隔离变化点函数与通用函数
        做: 将来增加新功能时, 用lambda表达变化点
"""
list01 = [40, 5, 60, 7, 87, 89]


# 查找第一个大于50的数字
def find_single_gt_50():
    for item in list01:
        if item > 50:
            return item


# 查找第一个小于10的数字
def find_single_lt_10():
    for item in list01:
        if item < 10:
            return item


# 变化点函数
def condition01(item):  # 4
    return item > 50


# 新增需求: 查找第一个个位是7的数字
def condition02(item):
    return item % 10 == 7


# 通用函数
def find_single(condition):  # 2
    for item in list01:
        if condition(item):  # 3
            return item


print(find_single(condition01))  # 1
print(find_single(condition02))