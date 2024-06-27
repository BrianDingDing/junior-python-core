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
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

# map: 映射, 类似IterableHelper.select, 在员工列表中查找所有员工的姓名(一个员工映射一个姓名).
print(list(map(lambda emp: emp.name, list_employees)))

# filter: 过滤, 类似IterableHelper.find_all, 在员工列表中查找所有部门是9001的员工.
print(list(filter(lambda emp: emp.did == 9001, list_employees)))

# max/min: 最大/最小, 类似IterableHelper.get_max, 在员工列表中查找最有钱的员工
print(max(list_employees, key=lambda emp: emp.money))
print(min(list_employees, key=lambda emp: emp.money))

# sort: 排序, 修改旧列表, 类似IterableHelper.order_by, 根据工资对员工列表进行升序排列
# 升序排列
list_employees.sort(key=lambda emp: emp.money)
print(list_employees)
# 降序排列
list_employees.sort(key=lambda emp: emp.money, reverse=True)
print(list_employees)

# sorted: 返回新列表, 不改变旧列表
new_list_employees = sorted(list_employees, key=lambda emp: emp.money)
print(new_list_employees)

# 根据字典排序
dict01 = {"b": 2, "a": 100, "c": 3}
# 按照对key的编码值进行排序
print(sorted(dict01))  # ['a', 'b', 'c']
# 按照value进行排序, 返回key值
print(sorted(dict01, key=lambda key: dict01[key]))  # ['b', 'c', 'a']
# 按照value进行排序, 返回key, value
print(sorted(dict01.items(), key=lambda item: item[1]))  # [('b', 2), ('c', 3), ('a', 100)]
# 转为字典
print(dict(sorted(dict01.items(), key=lambda item: item[1])))  # {'b': 2, 'c': 3, 'a': 100}

# 条件: 工资大于20000, 并根据eid降序, 获取所有员工名字
print(
    list(
        map(
            lambda emp: emp.name,
            sorted(
                filter(lambda emp: emp.money > 20000, list_employees),
                key=lambda emp: emp.eid,
                reverse=True
            )
        )
    )
)
