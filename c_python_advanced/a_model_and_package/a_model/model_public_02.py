"""
    模块变量
"""
# 当前模块是主模块(第一次运行的模块)时: 存储为__main__
# 当前模块是被导入模块: 存储为真实模块名
# 直接运行model_public_02.py: 输出结果为__main__
# model_demo_02.py: 输出结果为model_public_02
print(__name__)