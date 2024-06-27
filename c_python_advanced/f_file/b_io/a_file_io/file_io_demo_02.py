"""
   文件内容搜索器, 根据迭代器三个字搜索文件名
"""
from pathlib import Path

p1 = Path.cwd().parent.parent.parent

for item in p1.rglob("*demo*.py"):
    with open(item, "r", encoding="utf-8") as file:
        if "迭代器" in file.read():
            print(file.name)
