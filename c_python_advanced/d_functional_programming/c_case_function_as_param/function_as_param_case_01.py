from common.iterable_tools import IterableHelper

list01 = [40, 5, 60, 87, 7, 89]

# 1. 查找第一个大于50的数字
print(IterableHelper.find_single(list01, lambda item: item > 50))

# 2. 查找第一个个位是7的数字
print(IterableHelper.find_single(list01, lambda item: item % 10 == 7))
