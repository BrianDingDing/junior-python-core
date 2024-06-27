"""
    装饰器
        原理: 在不改变旧功能定义与调用的情况下, 为其增加新功能
        闭包:
            有外有内: 外函数负责接收旧功能, 内函数负责包新旧功能
            内(函数)使用外(变量): 需要新旧功能同时执行, 外指的是旧功能函数, func变量
            外(函数)返回内(函数): 希望在调用旧功能(old_func())时执行wrapper()
"""

"""
# 方式一
def new_func():
    print("新功能")


def old_func():
    print("旧功能")


# 旧功能 = 新功能
# 缺点: 旧功能不再执行
old_func = new_func
old_func()
"""

"""
# 方式二
# 缺点: 新旧函数执行时间太早, 想在old_func()才执行
def new_func(func):
    print("新功能")
    func()  # 执行旧功能


def old_func():
    print("旧功能")


old_func = new_func(old_func)
old_func()
"""


def new_func(func):
    def wrapper():
        print("新功能")
        func()  # 执行旧功能
    return wrapper


def old_func():
    print("旧功能")


old_func = new_func(old_func)  # 调用外函数
old_func()  # 调用内函数
