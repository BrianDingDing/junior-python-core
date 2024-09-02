"""
    累加10-60整数, 个位不是3, 5, 8的整数和.
"""
# range用法
# 1. range(开始, 结束, 间隔), 不包含结束值
# 2. range(开始, 结束), 间隔默认是1
# 3. range(结束), 开始默认为0

sum_value = 0
for item in range(10, 61):
    i = item % 10
    if i == 3 or i == 5 or i == 8:
        continue
    sum_value += item
print("total: %d" % sum_value)
