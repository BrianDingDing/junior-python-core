"""
    函数内存分析
"""


# 1. 将函数代码加入到内存代码区
def func01(p1, p2):
    data = p1 + p2
    return data


num01 = 10
# 2. 调用函数时会在内存中开辟一块空间
# 存储函数内部创建的变量
res = func01(num01, 20)

# 3. 函数执行后,该空间立即释放
print(res)
