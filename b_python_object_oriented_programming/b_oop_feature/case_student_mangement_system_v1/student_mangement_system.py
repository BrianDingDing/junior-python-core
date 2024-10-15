"""
    MVC: 视图View 模型Model 控制器Controller
"""
# 准备 类型标注
from typing import List


class StudentModel:
    """
        学生数据模型: 封装View与Controller之间数据
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        self.sid = sid  # 全球唯一标识符

    def __str__(self):
        return "%s的编号是%s,年龄是%s,成绩是%s" % (self.name, self.sid, self.age, self.score)

    def __eq__(self, other):
        return self.sid == other


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

    def __input_student(self):
        model = StudentModel()
        model.name = input("请输入学生姓名: ")
        model.age = int(input("请输入学生年龄: "))
        model.score = int(input("请输入学生成绩: "))
        self.__controller.add_student(model)

    def __display_student(self):
        for item in self.__controller.list_student:
            # print("%s的编号是%s,年龄是%s,成绩是%s" % (item.name, item.sid, item.age, item.score))
            print(item)  # 打印Model对象, 自动执行Model的__str__

    def __delete_student(self):
        sid = int(input("请输入需要删除的学生编号: "))
        if self.__controller.remove_student(sid):
            print("亲~删除成功喽~")
        else:
            print("哦no~,失败了")

    def __modify_student(self):
        model = StudentModel()
        model.sid = int(input("请输入需要修改的学生编号:"))
        model.name = input("请输入修改后的学生姓名:")
        model.age = int(input("请输入修改后的学生年龄:"))
        model.score = int(input("请输入修改后的学生成绩:"))
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


view = StudentView()
view.main()
