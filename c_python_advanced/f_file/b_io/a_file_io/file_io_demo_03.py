"""
    文本文件写入
"""
# 写入w: 文件不在会创建, 文件存在会覆盖
# 追加a: 文件不在会创建, 文件存在会在末尾增加新内容
with open("demo02.txt", "a", encoding="utf8") as file:
    file.write("白雪\n")
    file.write("夏文剑\n")

    # 多个元素写入到文件,不会换行
    file.writelines(["白雪", "夏文剑"])
