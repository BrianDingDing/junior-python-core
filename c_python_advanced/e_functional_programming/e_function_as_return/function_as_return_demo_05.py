"""
    为sum_data, 增加打印函数执行时间的功能.
    函数执行时间公式: 执行后时间 - 执行前时间
"""
import time


def print_execution_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("执行时间: %s" % (end - begin))
        return result

    return wrapper


@print_execution_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(sum_data(100000000))
