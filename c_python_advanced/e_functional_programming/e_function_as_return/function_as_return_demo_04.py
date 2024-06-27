"""
    装饰器:
    1. 内函数的返回值必须是旧功能的返回值
    2. 参数设计思想: 调用者调用新旧功能函数(wrapper函数)时, 把多参数通过*args(星号元组形参)变成一容器,
                   新旧功能函数(wrapper函数)调用旧功能函数(func函数), 把一容器通过*args(序列实参)变成多参数.
"""


def new_func(func):  # 2
    def wrapper(*args, **kwargs):  # 4      多合一
        print("新功能")
        res = func(*args, **kwargs)  # 5    一拆多
        return res

    return wrapper


# old_func1 = new_func(old_func1)  # 1
# 1. 调用new_func, 2. 并把old_func1传入了new_func, 3. 返回的wrapper函数赋值给old_func1
@new_func
def old_func1(a):  # 6
    print("参数是：", a)
    return 100


# old_func2 = new_func(old_func2)  # 1
@new_func
def old_func2(a, b):  # 6
    print("参数是：", a, b)
    return 200


print(old_func1(10))  # 3
print(old_func2(10, 20))  # 3
print(old_func2(10, b=20))  # 3
print(old_func2(a=10, b=20))  # 3
