class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    # 相加: 返回新对象
    def __add__(self, other):
        if type(other) == Vector:
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other
        return Vector(x, y)

    # 累加: 返回旧对象
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


pos01 = Vector(1, 2)
pos02 = Vector(3, 4)
pos03 = pos01 + pos02  # pos01.__add__(pos02)
print(pos03)  # (4, 6)

pos03 = pos01 + 6  # pos01.__add__(6)
print(pos03)  # (7, 8)

print("--------")
pos01 = Vector(1, 2)
pos02 = Vector(3, 4)
print(id(pos01))  # 2292254679440
pos01 += pos02  # pos01.__iadd__(pos02)
print(id(pos01))  # 2292254679440
print(pos01)  # (4, 6)

# 笔试题: 下列2种写法完全相同吗?
# +=: 内部调用__iadd__, 返回自身对象; +: 内部调用__add__, 返回新对象.
# 元组等由于是不可变数据, 没有__iadd__方法, 即使调用+=, 也是调用__add__, 返回新对象.
# 但对于可变数据, +=会在原有对象上改变
print("~~~~~")
data01 = [1]
data02 = [2]
print(id(data01))  # 2292252890368

data01 += data02
print(id(data01))  # 2292252890368

data01 = data01 + data02
print(id(data01))  # 2292254610944
