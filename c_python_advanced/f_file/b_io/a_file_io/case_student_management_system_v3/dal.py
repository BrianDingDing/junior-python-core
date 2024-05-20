from pathlib import Path

from c_python_advanced.f_file.b_io.a_file_io.case_student_management_system_v3.dtl import StudentModel


class StudentDao:
    """
        学生数据访问对象: 将学生列表进行持久化处理
    """

    def __init__(self):
        self.__file_name = "student.txt"
        Path(self.__file_name).touch()

    def save(self, student_list):
        """
            将内存中的列表存入硬盘
        """
        with open(self.__file_name, "w", encoding="utf8") as file:
            file.write(student_list.__repr__())

    def load(self):
        """
            将硬盘中文件读取到内存中
        """
        with open(self.__file_name, "r", encoding="utf8") as file:
            content = file.read()
            if len(content) == 0:  # 没有历史数据
                return []
            # 有历史数据
            return eval(content)  # type: List[StudentModel]
