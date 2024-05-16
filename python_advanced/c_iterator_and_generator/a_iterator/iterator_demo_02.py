"""
    自定义可迭代对象 + 迭代器
"""


# 迭代器
class StudentIterator:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration()

        self.index += 1
        return self.data[self.index]


# 可迭代对象
class StudentController:
    def __init__(self):
        self.list_student = []

    def __iter__(self):
        return StudentIterator(self.list_student)


controller = StudentController()
controller.list_student.append("钟浩文")
controller.list_student.append("苏玉")
controller.list_student.append("鲁常为")

# for item in controller:
#     print(item)

iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
