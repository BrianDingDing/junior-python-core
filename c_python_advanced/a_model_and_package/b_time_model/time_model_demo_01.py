"""
    标准库模块: 时间模块
"""
import time

# 时间元组 (年,月,日,时,分,秒,星期几,年的第几天,夏令时)
tuple_time = time.localtime()
print(tuple_time[0])  # 年份
print(tuple_time[6])  # 星期几+1
print(tuple_time[-3])  # 星期
print(tuple_time[:3])  # 年,月,日
print(tuple_time[3:-3])  # 时,分,秒

# 机器时间: 1970年元旦到现在经过的秒数(时间戳)
print(time.time())

# 时间戳 --> 时间元组
print(time.localtime(1678673548.204874))

# 时间元组 --> 时间戳, 时间元组最小是秒, 因此时间戳小数点后面都没了.
print(time.mktime(tuple_time))

# 时间元组 --> 字符串
# 语法: 字符串 = time.strftime(格式, 时间元组)
print(time.strftime("%y/%m/%d %H:%M:%S", tuple_time))
print(time.strftime("%Y/%m/%d %H:%M:%S", tuple_time))
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒", tuple_time))

# 字符串 --> 时间元组
# 语法:时间元组 = time.strptime(字符串, 格式)
print(time.strptime("2023年03月13日 10时22分09秒", "%Y年%m月%d日 %H时%M分%S秒"))
