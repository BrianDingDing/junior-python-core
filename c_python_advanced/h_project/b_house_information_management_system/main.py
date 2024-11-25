"""
    房源信息管理系统
    1. 搭建MVC架构.
    2. 按1键显示所有房源信息.
    3. 按2键显示总价最贵的房源信息.
    - 使用max(自定义对象列表)实现, 需要重写__gt__.
    - 使用max(自定义对象列表, lambda)实现.
    4. 按3键根据面积升序显示房源信息.
"""

from c_python_advanced.h_project.b_house_information_management_system.usl import HouseView

if __name__ == '__main__':
    view = HouseView()
    view.main()
