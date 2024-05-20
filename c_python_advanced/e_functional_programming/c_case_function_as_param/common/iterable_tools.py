"""
    可迭代对象工具集
"""


class IterableHelper:
    """
        可迭代对象助手: 封装对可迭代对象的常用高阶函数
        高阶函数: 将函数作为参数或返回值的函数
    """

    @staticmethod
    def find_single(iterable, condition):
        """
            根据任意条件在可迭代对象查找第一个满足条件的元素
        :param iterable: 可迭代对象
        :param condition: 函数类型, 查找条件
        :return: 第一个满足条件的元素
        """
        for item in iterable:
            if condition(item):
                return item

    @staticmethod
    def find_all(iterable, condition):
        """
            在可迭代对象中查找所有满足条件的元素
        :param iterable: 需要搜索的可迭代对象
        :param condition: 函数类型, 查找条件
        :return: 生成器对象, 推算所有满足条件的元素
        """
        for item in iterable:
            if condition(item):
                yield item

    @staticmethod
    def select(iterable, condition):
        """
            在可迭代对象中, 根据条件选择元素的成员
        :param iterable: 可迭代对象
        :param condition: 函数类型, 选择的条件
        :return: 生成器, 推算所有选择的元素
        """
        for item in iterable:
            yield condition(item)

    @staticmethod
    def sum(iterable, condition):
        """
            根据任意条件累加可迭代对象中的元素
        :param iterable: 可迭代对象
        :param condition: 累加条件
        :return: 数值类型, 累加和
        """
        sum_value = 0
        for item in iterable:
            sum_value += condition(item)
        return sum_value

    @staticmethod
    def delete_single(iterable, condition):
        """
            删除可迭代对象中第一个满足条件的元素
        :param iterable: 可迭代对象
        :param condition: 函数类型, 搜索条件
        :return: boolean, 是否成功
        """
        for i in range(len(iterable)):
            if condition(iterable[i]):
                del iterable[i]
                return True
        return False

    @staticmethod
    def delete_all(iterable, condition):
        """
            删除可迭代对象中所有满足条件的元素
        :param iterable: 可迭代对象
        :param condition: 函数类型, 搜索条件
        :return: int, 删除数量
        """
        count = 0
        for i in range(len(iterable) - 1, -1, -1):
            if condition(iterable[i]):
                del iterable[i]
                count += 1
        return count

    @staticmethod
    def get_max(iterable, condition):
        """
            根据任意条件在可迭代对象中查找最大元素
        :param iterable: 可迭代对象
        :param condition: 函数类型, 查找条件
        :return: 最大元素
        """
        max_obj = iterable[0]
        for i in range(1, len(iterable)):
            if condition(max_obj) < condition(iterable[i]):
                max_obj = iterable[i]
        return max_obj

    @staticmethod
    def order_by(iterable, condition):
        """
            根据任意条件对可迭代对象升序排列
        :param iterable: 可迭代对象
        :param condition: 函数类型, 排序条件
        """
        for i in range(len(iterable) - 1):
            for j in range(i + 1, len(iterable)):
                if condition(iterable[i]) > condition(iterable[j]):
                    iterable[i], iterable[j] = iterable[j], iterable[i]

    @staticmethod
    def is_repeat(iterable, condition):
        """
            根据任意条件, 判断可迭代对象中是否包含相同的元素
        :param iterable: 可迭代对象
        :param condition: 函数类型, 判断条件
        :return: boolean, 是否包含
        """
        for i in range(len(iterable) - 1):
            for j in range(i + 1, len(iterable)):
                if condition(iterable[i]) == condition(iterable[j]):
                    return True
        return False
