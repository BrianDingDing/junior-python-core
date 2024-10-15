"""
   继承: 代码不用子类写, 但是可以直接用.
"""


# 适用性: 多个类型, 代码有共性, 概念还统一(学生是一种人类型)
class Person:
    def say(self):
        print("讲话")


class Student(Person):
    def study(self):
        print("学习")
        self.say()


s = Student()
s.say()
s.study()

# 对象 是一种 类型
# 学生对象 是一种 学生类型
print(isinstance(s, Student))  # True
# 学生对象 是一种 人类型
print(isinstance(s, Person))  # True
# 人对象 是一种 学生类型
p = Person()
print(isinstance(p, Student))  # False

# 类型 是一种 类型
# 学生类型 是一种 学生类型
print(issubclass(Student, Student))  # True
# 学生类型 是一种 人类型
print(issubclass(Student, Person))  # True
# 人类型 是一种 学生类型
print(issubclass(Person, Student))  # False

# 对象的类型 是 类型
# 学生对象的类型 是 学生类型
print(type(s) == Student)  # True
# 学生对象的类型 是 人类型
print(type(s) == Person)  # False
# 人对象的类型 是 学生类型
print(type(p) == Student)  # False
