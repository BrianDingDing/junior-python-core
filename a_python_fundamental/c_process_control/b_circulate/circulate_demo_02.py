"""
    在终端输入任意数字, 计算累加值
"""
number = input("insert number: ")
sum_value = 0
for item in number:  # number是str
    sum_value += int(item)
print("total: %d" % sum_value)
