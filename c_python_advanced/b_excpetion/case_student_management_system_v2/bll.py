from typing import List

from dtl import StudentModel


class StudentController:
    """
        学生控制器: 负责核心功能的算法
    """

    def __init__(self):
        self.list_student = []  # type:List[StudentModel]
        self.__start_id = 1001

    def add_student(self, new):
        # 自增长
        new.sid = self.__start_id
        self.__start_id += 1
        self.list_student.append(new)

    def remove_student(self, sid):
        # for i in range(len(self.list_student)):
        #     if self.list_student[i].sid == sid:
        #     if self.list_student[i].__eq__(sid):
        #         del self.list_student[i]
        #         return True
        # return False

        # 需要重写Model的__eq__方法
        if sid in self.list_student:
            self.list_student.remove(sid)
            return True
        return False

    def update_student(self, new):
        for item in self.list_student:
            if item.sid == new.sid:
                # item.name = new.name
                # item.age = new.age
                # item.score = new.score
                item.__dict__ = new.__dict__
                return True
        return False


# 当前模块为主模块时, 才执行测试代码. 项目发布后, 不执行测试代码
if __name__ == '__main__':
    controller = StudentController()
    controller.add_student(StudentModel())
    controller.add_student(StudentModel())
    controller.add_student(StudentModel())
    for item in controller.list_student:
        print(item)
