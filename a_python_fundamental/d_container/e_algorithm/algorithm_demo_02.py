list01 = [43, 45, 65, 67, 7, 8, 89]

for i in range(len(list01) - 1):  # 不要倒数第一个
    for j in range(i + 1, len(list01)):
        # 取出第i个元素与后面的元素(第j个)所有元素相比.
        if list01[i] < list01[j]:
            # 发现第i个元素后面的元素(第j个)更大, 则需要交换.
            list01[i], list01[j] = list01[j], list01[i]

print(list01)