"""
    内置生成器函数: enumerate
"""

list01 = [34, 54, 65, 67, 7687]

# 既能返回元素, 也能提供索引
# 快捷键: iter + 回车 / itere + 回车
for i, item in enumerate(list01):
    if item > 50:
        list01[i] = 50
