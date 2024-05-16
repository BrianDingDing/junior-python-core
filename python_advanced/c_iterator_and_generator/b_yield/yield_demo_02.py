"""
    生成器原理
"""
"""
class MyRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        number = 0
        while number < self.stop:
            yield number
            number += 1

obj = MyRange(5)
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
"""


def my_range(stop):
    number = 0
    while number < stop:
        yield number
        number += 1


# 创建了生成器对象
obj = my_range(5)

# 返回了相同的生成器对象
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

"""
不占内存原因: 生成器内部依赖__next__函数, 计算数据, 返回数据. 只存当前数据, 没有存储之前数据. 
class generator: # 生成器 = 可迭代对象 + 迭代器
    def __iter__(self):
        return self

    def __next__(self):
        计算数据
        return 数据 
"""
