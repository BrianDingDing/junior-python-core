"""
    二进制文件操作
"""

# 1. 文件拷贝
with open("test.png", "rb") as fr:
    # \x: 代表16进制
    # print(fr.read())

    with open("new.png", "wb") as fw:
        fw.write(fr.read())

print("abc")  # 字符串
print(b"abc")  # 字节串, 对应相应的ASCII编码

# 2. 加密
with open("test.png", "rb") as fr:
    with open("encrypt.png", "wb") as fw:
        # 先写干扰字符
        fw.write(b'123')
        # 再写正式数据
        fw.write(fr.read())

# 解密
with open("encrypt.png", "rb") as fr:
    with open("unencrypt.png", "wb") as fw:
        # 先读取干扰字符(不要数据, 只是让文件指针向后移动三个字节)
        fr.read(3)
        # 再读取正式数据
        fw.write(fr.read())

# 3. 高级点的加密
with open("test.png", "rb") as fr:
    with open("encrypt1.png", "wb") as fw:
        content01 = fr.read(20)  # 先读取20个字节
        content02 = fr.read()  # 再读取剩余字节
        fw.write(content02)
        fw.write(content01)

# 解密
with open("encrypt1.png", "rb") as fr:
    with open("unencrypt1.png", "wb") as fw:
        content = fr.read()
        content01 = content[-20:]
        content02 = content[:-20]
        fw.write(content01)
        fw.write(content02)

