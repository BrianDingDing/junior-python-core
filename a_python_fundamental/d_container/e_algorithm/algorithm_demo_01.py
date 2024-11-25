"""
    排序算法: 寻找最值
"""
list01 = [43, 45, 65, 167, 7, 8, 89]

max_value = list01[0]

# for item in list01[1:]:  # 切片读取数据会触发浅拷贝
for i in range(1, len(list01)):
    if max_value < list01[i]:
        max_value = list01[i]
print(max_value)
