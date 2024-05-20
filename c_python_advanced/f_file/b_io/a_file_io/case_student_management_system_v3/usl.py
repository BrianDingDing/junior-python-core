from c_python_advanced.f_file.b_io.a_file_io.case_student_management_system_v3.bll import StudentController
from c_python_advanced.f_file.b_io.a_file_io.case_student_management_system_v3.dtl import StudentModel


class StudentView:
    """
        学生视图: 处理界面逻辑, 输入输出...
    """

    def __init__(self):
        self.__controller = StudentController()

    def __display_menu(self):
        print("按1键录入学生信息")
        print("按2键显示学生信息")
        print("按3键删除学生信息")
        print("按4键修改学生信息")

    def __select_menu(self):
        number = input("请输入: ")
        if number == "1":
            self.__input_student()
        elif number == "2":
            self.__display_student()
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__modify_student()

    def __get_number(self, message):
        while True:
            try:
                number = int(input(message))
                return number
            except:
                pass

    def __input_student(self):
        model = StudentModel()
        model.name = input("请输入学生姓名: ")
        model.age = self.__get_number("请输入学生年龄: ")
        model.score = self.__get_number("请输入学生成绩: ")
        self.__controller.add_student(model)

    def __display_student(self):
        for item in self.__controller.list_student:
            print(item)  # 打印Model对象, 自动执行Model的__str__

    def __delete_student(self):
        sid = self.__get_number("请输入需要删除的学生编号: ")
        if self.__controller.remove_student(sid):
            print("亲~删除成功喽~")
        else:
            print("哦no~,失败了")

    def __modify_student(self):
        model = StudentModel()
        model.sid = self.__get_number("请输入需要修改的学生编号:")
        model.name = input("请输入修改后的学生姓名:")
        model.age = self.__get_number("请输入修改后的学生年龄:")
        model.score = self.__get_number("请输入修改后的学生成绩:")
        if self.__controller.update_student(model):
            print("噢耶~成啦...")
        else:
            print("no~好像不存在哦~")

    def main(self):
        """
            主逻辑: 程序入口
        """
        while True:
            self.__display_menu()
            self.__select_menu()
