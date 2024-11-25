"""
    内置可重写函数: 在某种条件下, 自动执行的函数(创建对象时, 执行__init__; 打印自定义对象, 执行__str__), 可以在自定义类型中进行重写.
    重写: 在子类中定义与父类相同的方法, 为了改变父类的行为, 体现子类的个性.
"""


class Person(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 自定义对象转换为字符串的格式
    def __str__(self):
        return "我是%s, 今年%s岁了" % (self.name, self.age)


xwj = Person("夏文剑", 26)
print(xwj)  # print(自定义对象), 会自动执行__str__
