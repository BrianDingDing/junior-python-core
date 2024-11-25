"""
    函数: 将做法与用法分离
          崇尚小而精, 拒绝大而全.
"""


# 1. 无参无返回值
def attack():
    print("直拳")
    print("摆拳")


attack()  # 函数调用


# 2. 有参无返回值
# 函数没有返回值, 默认返回为None.
def attack(count):  # 形参: 变量
    for item in range(count):
        print("直拳")
        print("摆拳")
        print("勾拳")


res = attack(2)  # 实参: 数据
print(res)  # None


# 3. 有参有返回值
def add(one, two):
    result = one + two
    return result


data = add(6, 2)
print(data)

