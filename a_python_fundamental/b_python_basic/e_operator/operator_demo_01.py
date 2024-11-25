"""
    数学运算符: + - *
    ** 幂运算; / 小数商; // 整数商; % 余数
"""
data01 = 5
data02 = 2
print(data01 ** data02)  # 25

seconds = int(input("请输入秒数:"))
minute = seconds // 60
second = seconds % 60
print(str(seconds) + "秒数是" + str(minute) + "分零" + str(second) + "秒")
