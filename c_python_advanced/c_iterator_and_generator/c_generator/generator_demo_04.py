"""
    列表: 优点: 可以反复使用, 支持索引切片
         缺点: 占用内存较大
    生成器: 优点: 节省内存
           缺点: 只能使用一次(返回旧的迭代器, 自身对象); 不支持索引与切片(不存储数据)
           适用性: 优先
    结论: 函数返回多个结果使用yield
         函数返回单个结果使用return
"""
list01 = [34, 45, 5, 6576, 8]


def find_number_gt_50():
    for item in list01:
        if item > 50:
            yield item


data = find_number_gt_50()

for item in data:
    print(item)
for item in data:
    print(item)

# list01.__iter__() # 创建新迭代器
# data.__iter__() # 返回自身对象

# print(data[-1]) # 生成器不支持索引, 因为都不存储数据

# 解决方案: 将函数返回值由生成器改为列表
data = list(find_number_gt_50())



