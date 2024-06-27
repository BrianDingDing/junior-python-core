# 1. 选择 / 填空
a = {"a": 1, "b": 2, "c": 3}
print(max(a))  # c
print(max(a, key=lambda x: a[x]))  # c

print("---" * 20)

a = [("a", 3), ("b", 2), ("d", 0)]
print(sorted(a, key=lambda x: x[1]))  # [('d', 0), ('b', 2), ('a', 3)]

print("---" * 20)

print(list(map(lambda x: x * x, [y for y in range(3)])))  # [0, 1, 4]

print("---" * 20)

# 2. tuple_database = (("张三",22,"男"),("李四",26,"女"))
#    转换为[{'name': '张三', 'age': 22, 'sex': '男'}, {'name': '李四', 'age': 26, 'sex': '女'}]
tuple_database = (("张三", 22, "男"), ("李四", 26, "女"))

# 方法一
print(
    list(
        map(
            lambda item: {"name": item[0], "age": item[1], "sex": item[2]},
            tuple_database
        )
    )
)

# 方法二
print(
    list(
        map(
            lambda item: dict(zip(["name", "age", "sex"], item)),
            tuple_database
        )
    )
)

print("---" * 20)

# 3. 给定一串字典(或列表), 找出指定的(前N个)最大值和最小值
# 字典序列或列表序列: [{}, {}, ...] / ({}, {}, ...) / [[], [], ...] / ([], [], ...)

list01 = [[2], [5], [8], [1]]
list02 = [{"a": 2}, {"a": 5}, {"a": 8}, {"a": 1}]
count = 2


def get_most_value(iterable, condition, n):
    max_value = iterable[0]
    min_value = iterable[0]

    for i in range(1, n):
        if condition(iterable[i]) > condition(max_value):
            max_value = iterable[i]
        if condition(iterable[i]) < condition(min_value):
            min_value = iterable[i]
    return max_value, min_value


print(get_most_value(list01, lambda item: item[0], 3))
print(get_most_value(list02, lambda item: item["a"], 3))

print("---" * 20)

# 4. 字典根据键升序排列
dic = {"name": "zs", "age": 18, "city": "深圳", "tel": 1383838438}


# 方法一: 自定义高阶函数
def order_by(iterable, condition):
    for i in range(len(iterable) - 1):
        for j in range(i + 1, len(iterable)):
            if iterable[i] > iterable[j]:
                iterable[i], iterable[j] = iterable[j], iterable[i]


items = list(dic.items())  # [('name', 'zs'), ('age', 18), ('city', '深圳'), ('tel', 1383838438)]
order_by(items, lambda item: item[0])
print(dict(items))  # {'age': 18, 'city': '深圳', 'name': 'zs', 'tel': 1383838438}

# 方法二: 内置高阶函数
print(dict(sorted(dic.items(), key=lambda item: item[0])))
