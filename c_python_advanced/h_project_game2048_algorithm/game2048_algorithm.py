list_merge = [2, 0, 0, 2]


# 1. 定义函数　zero_to_end()
# [2,0,2,0] --> [2,2,0,0]
def zero_to_end():
    """
        零元素向后移动: 从后向前判断, 如果是0则删除, 在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# zero_to_end()
# print(list_merge)


# 2. 定义函数　merge()
# [2,0,0,2] --> [2,2,0,0] --> [4,0,0,0]
def merge():
    """
        合并数据: 判断是否相邻相同. 如果是则合并, 在末尾追加0.
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]  # 4 2 0 0
            del list_merge[i + 1]  # 4 0 0
            list_merge.append(0)  # 4 0 0 0


# merge()
# print(list_merge)

map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]


# 3. 向左移动
def move_left():
    """
        向左移动map: 获取每行, 交给list_merge, 在通知merge()进行合并.
    """
    global list_merge
    for line in map:
        list_merge = line
        # merge函数内部操作的数据就是map行数据
        merge()


# move_left()
# print(map)


# 4. 向右移动
def move_right():
    """
        向右移动map
    """
    global list_merge  # [2,4,0,0]
    for line in map:
        # 从右向左获取数据形成新列表
        list_merge = line[::-1]  # [0,0,4,2]
        # 处理数据
        merge()  # [4,2,0,0]
        # 将处理后的数据再从右向左还给map
        line[::-1] = list_merge  # [0,0,2,4]


# move_right()
# print(map)


# 5. 方阵转置: 列转换为行
def square_matrix_transposition():
    new_map = [list(item) for item in zip(*map)]
    # map = new_map # 右边的整体给左边赋值
    map[:] = new_map  # 右侧左边每一个元素给左边每一个元素赋值


# square_matrix_transposition()
# print(map)


# 6. 向上移动 move_up
def move_up():
    """
        向上移动: 转置 -> move_left -> 转置　
    """
    square_matrix_transposition()
    move_left()
    square_matrix_transposition()


# move_up()
# print(map)


# 7. 向下移动 向下移动
def move_down():
    """
        向下移动: 转置 -> move_right -> 转置
    """
    square_matrix_transposition()
    move_right()
    square_matrix_transposition()


move_down()
print(map)
