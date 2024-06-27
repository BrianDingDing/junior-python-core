# 我过去, 导入文件, 适合面向过程(全局变量/函数).
# import 模块名
import model_public_01

# 模块名.成员名
model_public_01.func01()


# 你过来, 导入文件的内容, 适合面向对象(类).
# from 模块 import 成员
# 注意: 命名冲突
# from model_public_01 import func01,func02
# from model_public_01 import *
from model_public_01 import func01 as f1


def func01():
    print("haha...")


# 直接使用成员
func01()
f1()
