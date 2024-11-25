# 1. 选择 / 填空

# 可以执行代码, 可以创建对象, 但不能调用show方法.
# python是解释型编程语言, 程序自上而下运行, 翻译一条, 执行一条语句.
# 由于没调用show方法, 就不翻译和执行. 但会把show方法放进内存且不运行.
class Hello:
    def show(self):
        print(self.x)


# 2. 说出变量的特征
# (1) [面向过程] 全局变量: 整个文件都可以访问.
a2 = 10
# (2) [面向过程] 全局变量 + 隐藏成员: 使用from 模块 import * 导入时不饿能使用该成员, 但如果其他方式 (e.g from 模块 import _b) 导入则可以使用.
_b2 = 10


class A:
    def __init__(self):
        # a. [面向对象] 实例变量: 通过对象使用
        self.c2 = 10
        # b. [面向对象] 实例变量 + 隐藏成员: 不建议被导入使用.
        self._d2 = 10
        # c. [面向对象] 实例变量 + 私有变量: 只能本类通过对象使用.
        self.__e2 = 10
        # (3) [面向过程] 局部变量: 只能在当前方法(函数中)使用
        f = 10


# 3. 填空题
a3 = [1, 2, 3]
b3 = [4, 5]
# a3.append(b3)  # [1, 2, 3, [4, 5]]
# a3 += b3  # [1, 2, 3, 4, 5]
a3.extend(b3)  # [1, 2, 3, 4, 5]


# 4. 实现一个斐波拉契数列
# 方法一: 列表版本
def get_fibonacci_list(n):
    fibs = [1, 1]
    for __ in range(n - 2):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs


print(get_fibonacci_list(8))


# 方法二: 生成器版本
def get_fibonacci_generator(n):
    num01, num02 = 1, 1
    yield num01
    yield num02
    for __ in range(n - 2):
        num01, num02 = num02, num01 + num02
        yield num02


print(list(get_fibonacci_generator(8)))
