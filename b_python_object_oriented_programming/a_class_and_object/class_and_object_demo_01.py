# 1. 定义类
class Person:
    # 数据成员: 实例变量
    def __init__(self, name, height=170, sex="男"):
        # 生成形式参数快捷键: alt + 回车
        self.height = height
        self.name = name
        self.sex = sex

    # 行为成员: 实例方法
    def work(self):
        print(self.name, "在工作")


# 2. 创建对象
person = Person("丁丁", 180, "男")
person.work()
