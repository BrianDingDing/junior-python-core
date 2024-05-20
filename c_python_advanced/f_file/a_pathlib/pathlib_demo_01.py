"""
    路径和文件表示
"""
from pathlib import Path

# 相对路径
# print(Path("./pathlib_demo_01.py").exists())
print(Path("pathlib_demo_01.py").exists())
print(Path("../../c_iterator/iterator_demo_02.py").exists())

# 绝对路径
# 当前工作目录的绝对路径
print(Path.cwd())  # G:\Repository\Python\Junior Python\junior-python-core\c_python_advanced\f_file\a_pathlib
print(Path.cwd().parent.parent.joinpath("c_iterator", "iterator_demo_02.py").exists())

"""
返回都是自身self, 即路径对象
class Path: 

    @staticmethod
    def cwd():
        pass
        return self

    def parent(self):
        pass
        return self

    def joinpath(self):
        pass
        return self

    def exists(self):
        pass
"""
