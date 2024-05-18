"""
    yield
"""


class StudentController:
    def __init__(self):
        self.list_student = []

    def __iter__(self):

        # 自动生成迭代器的大致规则:
        # 1. 将yield以前的代码定义在__next__函数中
        # 2. 将yield以后的数据作为__next__函数返回值

        index = 0
        yield self.list_student[index]
        index += 1
        yield self.list_student[index]
        index += 1
        yield self.list_student[index]

        # 最后一次next(), raise StopIteration()


controller = StudentController()
controller.list_student.append("a")
controller.list_student.append("b")
controller.list_student.append("c")

# for item in controller:
#     print(item)

iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
