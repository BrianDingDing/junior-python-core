"""
     lambda应用: 作为高阶函数的实参
"""
list01 = [40, 5, 60, 7, 87, 89]


def find_single(condition):
    for item in list01:
        if condition(item):
            return item


# def condition01(item):
#     return item > 50

# print(find_single(condition01))
print(find_single(lambda item: item > 50))
