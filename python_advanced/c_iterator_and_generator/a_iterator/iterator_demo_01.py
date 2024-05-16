"""
    迭代 iteration: 重复获取下一个元素的过程
    迭代器 iterator: 完成迭代过程的对象, 具有__next__函数
    可迭代对象 iterable: 创建迭代器的对象, 具有__iter__函数
"""

# for循环原理
# 1. 获取迭代器对象
message = "abcdefghj"
iterator = message.__iter__()

while True:
    try:
        # 2. 循环获取下一个元素
        item = iterator.__next__()
        print(item)

        # 3. 如果停止迭代, 退出循环
    except StopIteration:
        break

# 笔试题: 请简述, 对象能够参与for循环的条件是什么?
# 答: 对象必须具有__iter__函数, 必须是可迭代对象.