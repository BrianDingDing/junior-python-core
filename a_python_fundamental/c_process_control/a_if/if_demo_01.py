"""
    根据心理年龄与实际年龄, 打印智商等级.
    智商IQ = 心理年龄MA 除以 实际年龄CA 乘以 100
"""
ma = int(input("心理年龄: "))
ca = int(input("实际年龄: "))
iq = ma / ca * 100
if iq >= 140:
    print("天才")
elif iq >= 120:  # 如果能执行到本行, 一定小于140.
    print("超常")
elif iq >= 90:
    print("正常")
elif iq >= 80:
    print("迟钝")
else:
    print("低能")
