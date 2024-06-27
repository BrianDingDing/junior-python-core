from typing import List

from c_python_advanced.f_file.b_io.a_file_io.case_student_management_system_v3.dal import StudentDao
from c_python_advanced.f_file.b_io.a_file_io.case_student_management_system_v3.dtl import StudentModel


class StudentController:
    """
        学生控制器: 负责核心功能的算法
    """

    def __init__(self):
        # self.list_student = []  # type:List[StudentModel]
        self.__dao = StudentDao()
        self.list_student = self.__dao.load()  # type:List[StudentModel]
        if len(self.list_student) == 0:
            self.__start_id = 1001
        else:
            self.__start_id = self.list_student[-1].sid + 1

    def add_student(self, new):
        new.sid = self.__start_id
        self.__start_id += 1
        self.list_student.append(new)
        # 同步到硬盘中
        self.__dao.save(self.list_student)

    def remove_student(self, sid):
        if sid in self.list_student:
            self.list_student.remove(sid)
            # 同步到硬盘中
            self.__dao.save(self.list_student)
            return True
        return False

    def update_student(self, new):
        for item in self.list_student:
            if item.sid == new.sid:
                item.__dict__ = new.__dict__
                # 同步到硬盘中
                self.__dao.save(self.list_student)
                return True
        return False
