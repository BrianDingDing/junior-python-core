class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 给人看的, 没有语法约束的支持
    def __str__(self):
        return "我是%s,今年%s岁了" % (self.name, self.age)

    # 给机器执行的, 必须符合python语法规定
    def __repr__(self):
        return 'Person("%s",%s)' % (self.name, self.age)


print(eval("1+2"))  # 将字符串作为代码执行

xwj = Person("夏文剑", 26)

# 自定义对象的浅拷贝
message = xwj.__repr__()
obj = eval(message)
xwj.name = "文剑"
print(xwj)  # 我是文剑,今年26岁了
print(obj)  # 我是夏文剑,今年26岁了
