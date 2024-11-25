from c_python_advanced.h_project.b_house_information_management_system.dtl import HouseModel


class HouseDao:
    """
        数据访问对象:负责数据的持久化处理
    """

    def __init__(self):
        self.file_name = 'house.txt'

    def load(self):
        """
            加载
        """
        with open(self.file_name, "r", encoding="utf-8") as fr:
            content = fr.read()
            if not content:
                return []
            return eval(content)  # type: List[HouseModel]
