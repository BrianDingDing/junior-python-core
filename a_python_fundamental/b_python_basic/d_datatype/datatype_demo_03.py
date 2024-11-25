"""
    字节串数据类型
    所有的字符串都能转换为字节串
    不是所有的字节串都可以转换为字符串
"""

# 代表的是数据的二进制内容, 这种写法只支持ascii字符
byte01 = b"Hello world"
print(type(byte01))
print(byte01)  # 只是为了巧妙的展示. 0和1你也看不懂.

# 带有中文字符的字符串, 需要通过encode()转换才能变为字节串.
byte02 = "你好".encode(encoding="utf-8")
print(byte02)

# 由字节串转换为字符串
print(byte02.decode("utf-8"))
