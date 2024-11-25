"""
    索引: 定位单个元素, 语法: 容器名[整数].
    注意: 整数从0开始到len(容器名)-1.
         整数从-1开始到-len(容器名).
"""
message = "我是花果山水帘洞美猴王孙悟空"
print(message[0])  # 我
print(message[2])  # 花
print(message[len(message) - 1])  # 空
# print(message[99]) # IndexError: string index out of range
print(message[-1])  # 空
# print(message[-99]) # IndexError: string index out of range
