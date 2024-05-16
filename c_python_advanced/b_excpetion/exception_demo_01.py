"""
    异常处理
        适用性: 不处理语法错误, 而是针对逻辑错误(往往因为数据超过有效范围而引起的错误)
        价值：让程序能够按照既定流程执行,不紊乱
"""


# NameError
# print(name)

# TypeError
# print(1 + "1")

# IndexError
# list01 = []
# print(list01[0])

# AttributeError
# class MyClass:
#     pass

# m = MyClass()
# print(m.name)

# 语法1: 包治百病
def div_apple(apple_count):
    try:
        # ValueError
        person_count = int(input("请输入人数:"))
        # ZeroDivisionError
        result = apple_count / person_count
        print(f"每人分{result}个苹果")
    except:  # except Exception:
        print("程序出错了")


div_apple(10)
print("后续逻辑")

# 语法2: 对症下药(官方建议)
"""
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数: "))
        result = apple_count / person_count
        print(f"每人分{result}个苹果")
    except ValueError:
        print("程序出错了, 输入了非整数")
    except ZeroDivisionError:
        print("程序出错了, 输入了零")

div_apple(10)
print("后续逻辑")
"""

# 语法3: 无论对错, 都必须执行的逻辑
"""
def div_apple(apple_count):
    try:
        person_count = int(input("请输入人数: "))
        result = apple_count / person_count
        print(f"每人分{result}个苹果")
    finally:
        print("分苹果结束了")

div_apple(10)
print("后续逻辑")
"""