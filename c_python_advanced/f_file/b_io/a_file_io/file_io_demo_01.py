"""
    文本文件操作流程
"""
# 写法比较麻烦
# 1. 打开
# 只要创建python文件都以utf8编码, 但windows: 默认打开文件(open函数)方式是GBK, Linux则是utf8
# file = open("file_io_demo_01.py", "r", encoding="utf-8")
# try:
#     # 2. 操作
#     print(file.read())
# finally:
#     # 3. 关闭
#     file.close()

# 写法简单
# 1. 打开
# with open("file_io_demo_01.py", "r", encoding="utf-8") as file:
#     # 2. 操作
#     print(file.read())
# # 离开缩进, 解释器负责关闭文件

with open("file_io_demo_01.py", "r", encoding="utf-8") as file:
    # 读取全部文件
    # print(file.read())

    # 根据字符数量读取文件, 读取3个字符
    # print(file.read(3))

    # 把每一行读成列表
    # file.readlines()

    # 读取每行, 省内存(文件极大时使用)
    for item in file:
        print(item)
