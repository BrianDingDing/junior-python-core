"""
    程序产生一个1到100的随机数, 让玩家猜对为止
"""
import random

ran_num = random.randint(1, 100)
count = 0
print("随机数为:%d" % ran_num)

while True:
    count += 1
    guess_num = int(input("输入数字: "))
    if guess_num > ran_num:
        print("大了")
    elif guess_num < ran_num:
        print("小了")
    else:
        print("bingo, 总共猜了%d次" % count)
        break
