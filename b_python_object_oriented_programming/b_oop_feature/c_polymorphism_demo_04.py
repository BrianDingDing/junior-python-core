class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self):
        return 'Vector("%s",%s)' % (self.x, self.y)

    # 相同的依据
    def __eq__(self, other):
        # 默认按照地址比较
        # return id(self) == id(other)
        # 重写后按照内容比较
        return self.__dict__ == other.__dict__

    # 大小的依据
    def __gt__(self, other):
        return self.x > other.x


pos01 = Vector(1, 1)
pos02 = Vector(1, 1)
# 按照eq比较
print(pos01 == pos02)  # True
# 按照地址比较
print(pos01 is pos02)  # False
# 使用gt比较
print(pos01 < pos02)  # False

# Python语言的内存优化机制
# 对象池: 创建对象时, 会判断池中是否具有相同的对象
#        如果有会返回地址, 如果没有会开辟空间
# int/float/str/tuple/bool

# 列表没有对象池, 列表地址不一样; 但列表有__eq__函数, 按照内容比较; 没有__eq__函数, 按照地址比较.
print("~~~~~")
a = ["a", ["b"]]
b = ["a", ["b"]]
print(a == b)  # True
print(a is b)  # False

print("--------")
list_position = [
    Vector(0, 2),
    Vector(1, 1),
    Vector(5, 5),
    Vector(3, 3),
    Vector(1, 1),
]

# 内部: 向量与向量比较是否相同(__eq__函数)
print(Vector(1, 1) in list_position)  # True
print(list_position.count(Vector(1, 1)))  # 2
list_position.remove(Vector(3, 3))

# 内部: 向量比较大小(__gt__函数)
print(max(list_position))  # (5, 5)
print(min(list_position))  # (0, 2)
list_position.sort()
print(list_position)  # [Vector("0",2), Vector("1",1), Vector("1",1), Vector("5",5)]
