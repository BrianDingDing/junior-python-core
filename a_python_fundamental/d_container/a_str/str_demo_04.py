"""
    切片: 定位多个元素, 语法: 容器名[整数:整数:整数]
"""
message = "我是花果山水帘洞美猴王孙悟空"
# 1. 容器名[开始:结束:间隔], 不包含结束.
print(message[1:5:2])  # 是果

# 2. 容器名[开始:结束], 间隔默认为1.
print(message[1:5])  # 是花果山

# 3. 容器名[:结束], 开始默认为头.
print(message[:5])  # 我是花果山

# 4. 容器名[:], 结束默认为尾巴
print(message[-3:])  # 孙悟空
print(message[:])  # 全部

# 5. 特殊: 倒序
print(message[::-1])  # 空悟孙王猴美洞帘水山果花是我

message = "我是花果山水帘洞美猴王孙悟空"
print(message[2:-3])  # 花果山水帘洞美猴王
print(message[2:2])  # 不报错,没有定位到元素
print(message[2:99])  # 越界不报错, 花果山水帘洞美猴王孙悟空
print(message[6:3:-1])  # 帘水山
