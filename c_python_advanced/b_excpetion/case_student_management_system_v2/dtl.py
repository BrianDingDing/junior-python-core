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
