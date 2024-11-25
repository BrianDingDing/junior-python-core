class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


# 子类若没有构造函数, 直接使用父类继承而来的
class Student(Person):
    pass


# 子类有构造函数会覆盖父类的构造函数, 从而使用自己的构造函数
# 此时子类必须通过super函数调用父类构造函数
class Teacher(Person):
    # 子类构造函数参数: 父类+子类
    def __init__(self, name, age, salary=0):
        super().__init__(name, age)
        self.salary = salary


# 执行父类构造函数.
# debug时候, Person类的self指向的是zwx对象.
zxw = Student("aa", 26)

qtx = Teacher("bb", 26, 10000000)
print(zxw.__dict__)
print(qtx.__dict__)
