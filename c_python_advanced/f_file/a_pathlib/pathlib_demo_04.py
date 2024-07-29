"""
    路径和文件操作
"""
from pathlib import Path

# 1. 创建
# (1) 文件, 如果存在不创建, 不存在才创建.
Path("demo.txt").touch()

# (2) 目录, 如果存在报错, 不存在才创建.
# Path("a").mkdir()

# 如果存在也不报错
Path("a").mkdir(exist_ok=True)

# # 创建b目录,b.txt文件
Path("b").mkdir(exist_ok=True)
Path("b", "b.txt").touch()

# 2. 重命名
# (1) 文件, 一定带后缀.
# Path("demo.txt").rename("A.txt")

# # (2) 文件夹的文件
# # 文件会从b目录中移出
# # Path("b","b.txt").rename("B.txt")
#
# 重命名目录中的文件名
# old = Path("b", "b.txt")
#
# # 生成基于原来路径的新文件名
# new_name = old.with_name("B.txt")  # 保持路径不变, "b/B.txt"
# old.rename(new_name)
#
# # 3. 删除
# (1) 文件, 如果文件不存在会报错
Path("A.txt").unlink()
# 文件不存在也不报错
Path("abc.txt").unlink(missing_ok=True)
#
# # (2) 目录, 如果目录不存在会报错
Path("a").rmdir()
# 目录不为空也会报错
# Path("b").rmdir()

import shutil

# 删除目录与内部所有文件, 找不回来
shutil.rmtree("b")
