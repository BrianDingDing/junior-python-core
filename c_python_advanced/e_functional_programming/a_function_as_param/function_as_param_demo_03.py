class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __str__(self):
        return "员工编号是%s,部门是%s,姓名是%s,工资是%s" % (self.eid, self.did, self.name, self.money)

    def __repr__(self):
        return 'Employee(%s, %s, %s, %s)' % (self.eid, self.did, self.name, self.money)


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


def condtion01(emp: Employee):  # 参数类型标注
    return emp.did == 9001


def condtion02(emp):
    return len(emp.name) == 2


def find_all(condition):
    for item in list_employees:
        if condition(item):
            yield item


# 1. 在员工列表中查找所有部门是9001的员工
obj = find_all(condtion01)
for emp in obj:
    print(emp.__dict__)

# 2. 在员工列表中查找所有姓名是2个字的员工
print(list(find_all(condtion02)))