"""
    lambda 匿名函数: 但是lambda只能有一条语句,且不能是赋值语句
"""
# 1. 有参数有返回值
# def func01(p1, p2):
#     return p1 > p2

func01 = lambda p1, p2: p1 > p2
print(func01(1, 2))

# 2. 无参数有返回值
# def func02():
#     return 250

func02 = lambda: 250
print(func02())

# 3. 无参数无返回值
# def func03():
#     print("hello world")

func03 = lambda: print("hello world")
func03()

# 4. 有参数无返回值
# def func04(p):
#     print("参数是：", p)

func04 = lambda p: print("参数是: ", p)
func04(10)


# 注意 1: lambda不支持多条语句
def func05():
    for item in range(10):
        print(item)


# lambda :for item in range(10):print(item)


# 注意 2: 不能是赋值语句
def func06(p):
    p[0] = 200


list01 = [10]
func06(list01)
print(list01)  # ?

# func06 = lambda p: p[0] = 200
