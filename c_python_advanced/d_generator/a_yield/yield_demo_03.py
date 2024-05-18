"""
    yield - 应用
"""
list01 = [432, 54, 56, 667, 67, 88, 9]


# 定义函数, 找出大于50的数字
# 思路1: 用列表存储所有结果
# 缺点: 占用内存较大
# def find_number_gt_50():
#     list_result = []
#     for item in list01:
#         if item > 50:
#             list_result.append(item)
#     return list_result
#
# data = find_number_gt_50()
# for item in data:
#     print(item)

# 思路2: 使用yield关键字返回结果
# 优点: 几乎不占内存
def find_number_gt_50():
    for item in list01:
        if item > 50:
            yield item


data = find_number_gt_50()
for item in data:
    print(item)
