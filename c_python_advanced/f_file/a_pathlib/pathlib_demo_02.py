"""
    路径和文件属性
    对象名.absolute()  # 绝对路径(路径类型)
    对象名.name  # 带后缀的完整文件名(str类型)
    对象名.stem  # 文件名不带后缀(str类型)
    对象名.suffix # 文件后缀(str类型)
    对象名.parent  # 上一级路径(路径类型)
    对象名.parts  # 分割路径(tuple类型)
    对象名.exists()  # 路径是否存在(bool类型)
    对象名.is_file()  # 是否文件(bool类型)
    对象名.is_dir()  # 是否目录(bool类型)
    对象名.is_absolute() # 是否绝对路径(bool类型)
    对象名.stat().st_ctime  # 创建时间(时间戳)
    对象名.stat().st_atime  # 访问时间(时间戳)
    对象名.stat().st_mtime  # 修改的时间(时间戳)
    对象名.stat().st_size  # 文件大小(字节Bete)
"""
import time
from pathlib import Path

p1 = Path("pathlib_demo_02.py")
print(p1.absolute())

p2 = Path.cwd()
print(p2.parts)
print(time.localtime(p2.stat().st_ctime))
print(p1.stat().st_size)
