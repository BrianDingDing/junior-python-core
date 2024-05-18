from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __repr__(self):
        return 'Employee(%s, %s, %s, %s)' % (self.eid, self.did, self.name, self.money)


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 70000),
    Employee(1003, 9002, "猪八戒", 70000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

# 1. 在员工列表中查找所有部门是9001的员工
print(list(IterableHelper.find_all(list_employees, lambda emp: emp.did == 9001)))

# 2. 在员工列表中查找所有姓名是2个字的员工
print(list(IterableHelper.find_all(list_employees, lambda emp: len(emp.name) == 2)))

# 3. 在员工列表中查找所有员工的姓名
print(list(IterableHelper.select(list_employees, lambda emp: emp.name)))

# 4. 在员工列表中查找所有员工的编号和工资
print(list(IterableHelper.select(list_employees, lambda emp: (emp.eid, emp.money))))

# 5. 累加所有员工的工资
print(IterableHelper.sum(list_employees, lambda item: item.money))

# 6. 累加所有员工的编号
print(IterableHelper.sum(list_employees, lambda item: item.eid))

# 7. 在员工列表中删除第一个部门是9001的员工
# IterableHelper.delete_single(list_employees, lambda item: item.did == 9002)

# 8. 在员工列表中删除第一个薪资小于30000的员工
# IterableHelper.delete_single(list_employees, lambda item: item.money < 30000)

# 9. 在员工列表中删除所有薪资小于50001的员工
# print(IterableHelper.delete_all(list_employees, lambda item: item.money < 50001))
# print(list_employees)

# 10. 在员工列表中查找最有钱的员工
print(IterableHelper.get_max(list_employees, lambda emp: emp.money))

# 11. 在员工列表中查找编号最大的员工
print(IterableHelper.get_max(list_employees, lambda emp: emp.eid))

# 12. 根据工资对员工列表进行升序排列
IterableHelper.order_by(list_employees, lambda emp: emp.money)
print(list_employees)

# 13. 判断员工列表中是否存在相同的工资
print(IterableHelper.is_repeat(list_employees, lambda emp: emp.money))
