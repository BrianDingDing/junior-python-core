"""
    函数参数
"""


# 1. 位置形参: 实参必须填写.
def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 缺少一个参数
# TypeError: func01() missing 1 required positional argument: 'p3'
# func01(1,2)

# 函数要3个参数但是给了4个
# TypeError: func01() takes 3 positional arguments but 4 were given
# func01(1,2,3,4)

print("---" * 30)


# 2. 默认形参: 实参可以选择; 注意: 默认形参必须从右向左依次存在.
def func02(p1=10, p2=0.0, p3=""):
    print(p1)
    print(p2)
    print(p3)


func02()
func02(1, 2.3, "4")
func02(1)
func02(1, 2.3)

print("---" * 30)


# 3. 位置实参和关键字实参
def func03(p1=10, p2=0.0, p3=""):
    print(p1)
    print(p2)
    print(p3)


# 位置实参: 按顺序与形参进行对应
func03(1, 2, "3")

# 关键字实参: 按名称与形参进行对应. 为了跳过某些参数.
func03(p3="3")
func03(p2=2.3, p3="3")
func03(1, p3="3")

print("---" * 30)


# 4. 星号元组形参: 将多个位置实参合并为一个元组
def func04(*args):
    print(args)


# 调用者无需构建容器, 而是由Python解析器构建
func04()
func04(1)
func04(1, 2)

print("---" * 30)


# 5. 双星号字典形参: 将多个关键字实参合并为一个字典
def func05(**kwargs):
    print(kwargs)


func05(p1=1, p2=2)

print("---" * 30)


def func06(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


# 6. 序列实参: 一序列拆分为多参数, 按顺序对应.
list01 = [1, 2, 3]
tuple01 = (1, 2, 3)
str01 = "夏文剑"

func06(*list01)
func06(*tuple01)
func06(*str01)

print("---" * 30)

# 7. 字典实参: 一字典拆分为多参数, 按名称对应.
dict01 = {"p3": 1, "p1": 2, "p2": 3}
func06(**dict01)

print("---" * 30)


# 8. 命名关键字形参(p1): 必须使用关键字实参传递.
def func07(*args, p1=0):
    print(args)
    print(p1)


func07(1)
func07(1, p1=2)
func07(1, 2, p1=3)
func07(p1=3)


# *修饰后面的参数为命名关键字形参, p2仍然是命名关键字形参, 必须使用关键字实参传递.
def func08(p1, *, p2=0):
    print(p1)
    print(p2)


func08(1, p2=2)
