"""
    类区分行为的不同, 对象区分数据不同
"""
# 情景描述: 老张开车去东北
# 分析:
#  老张     汽车
# 去东北    行驶

# 跨类调用 1: 直接创建对象. 语义: 老张每次开新车去东北
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self):
        print(self.name,"去东北")
        car = Car()
        car.run()

class Car:
    def run(self):
        print("汽车在行驶")

lw = Person("老王")
lz = Person("老张")
lz.go_to()
"""

# 跨类调用 2: 在构造函数中创建对象. 语义: 老张开自己的车去东北
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def go_to(self):
        print(self.name, "去东北")
        self.car.run()

class Car:
    def run(self):
        print("汽车在行驶")

lz = Person("老张")
lz.go_to()
"""


# 跨类调用 3: 通过参数传入对象. 语义: 老张通过交通工具去东北
class Person:
    def __init__(self, name=""):
        self.name = name

    def go_to(self, vehicle):
        print(self.name, "去东北")
        vehicle.run()


class Car:
    def run(self):
        print("汽车在行驶")


lz = Person("老张")
car = Car()
lz.go_to(car)
