"""
    私有化
        做法: 以双下划线命名
        本质: python解释器修改命名, 单下划线 + 类名 + 私有变量名
        目的: 让类外无法访问私有成员
"""


class MyClass:
    def __init__(self, data=0):
        self.__data = data

    def __func01(self):
        print("func01")

    # 公开成员
    def func02(self):
        print(self.__data)  # 本类可以访问私有成员
        self.__func01()


m = MyClass(10)
print(m.__dict__)  # {'_MyClass__data': 10}
# print(m._MyClass__data)  # 10, 强硬访问
m.func02()
