"""
    搜索目录
"""
from pathlib import Path

p1 = Path.cwd().parent.parent

# 搜索当前目录所有路径或文件(一层)
# for item in p1.iterdir():
#     print(item)

# 使用通配符搜索(一层), 正则匹配
# for item in p1.glob("[a-f]_*"):
#     print(item)

# for item in p1.glob("e_functional_programming/*as*"):
#     print(item)

# 使用通配符搜索(递归多层)
# for item in p1.rglob("*"):
#     print(item)

# 使用通配符搜索(递归多层), 正则匹配
# for item in p1.rglob("*demo*.py"):
#     print(item)

path_list = list(p1.rglob("*.py"))
# 找出文件最大的文件
print(max(path_list, key=lambda item: item.stat().st_size))
# 找出访问时间最早的文件
print(min(path_list, key=lambda item: item.stat().st_atime))