from c_python_advanced.e_functional_programming.c_case_function_as_param.common.iterable_tools import IterableHelper
from c_python_advanced.h_project.b_house_information_management_system.dal import HouseDao


class HouseController:
    """
        房源控制器:对核心功能进行逻辑处理,存储/移除..
    """

    def __init__(self):
        self.__dao = HouseDao()
        self.list_house = self.__dao.load()

    def get_max_total_price(self):
        # 方案1: 重写Model类的__gt__
        # 优点: 最简单
        # 缺点: 不灵活
        # return max(self.list_house)

        # 方案2: lambda
        # 优点: 最灵活
        # 缺点: 最麻烦(每次都需要重写定义)
        return max(self.list_house, key=lambda h: h.total_price)

    def get_order_by_area(self):
        # python的排序使用的是快排序, 并且内部使用C语言实现; 而我们的IterableHelper使用的是冒泡排序.
        return sorted(self.list_house, key=lambda h: h.area)

        # new_list = self.list_house[:]  # 不想改变原来数据
        # IterableHelper.order_by(new_list, lambda h: h.area)
        # return new_list


