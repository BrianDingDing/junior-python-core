"""
    函数式编程: 将函数赋值给变量
"""


def func01():
    print("func01")


# 函数返回值赋值给变量, 立即执行函数.
# a = func01()

# 将函数赋值给变量, 不执行函数.
a = func01
# 间接调用, 通过变量调用函数.
a()


def func02():
    print("func02")


# 做函数时, 没有固定搭配.
def func03(func):
    print("func03")
    # func02() # 直接调用: 固定搭配
    func()  # 间接调用: 灵活搭配


# 使用函数时, 选择func03和谁搭配, 灵活搭配.
func03(func02)  # 03 + 02
func03(func01)  # 03 + 01
