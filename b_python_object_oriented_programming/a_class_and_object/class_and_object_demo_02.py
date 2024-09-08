"""
    实例成员: 实例就是对象(具体化), 成员包括变量和方法.
    实例变量: 对象.变量名, 用于表达不同个体的不同数据.
    实例方法: 对象.方法名(数据)
            def 方法名(self, 参数):
                方法体
"""
# 全局变量, 在内存中只有1个
name = "柯洪浩"


class Person:
    def __init__(self, name):
        self.name = name

    def work(self):
        pass


jian_ning = Person("丁丁")
jian_ning.name += "公主"
jian_ning.work()
print(jian_ning.name)

# 对象的属性, 用于存储自身实例变量的字典
print(jian_ning.__dict__)

# class Person:
#     pass
#
# # 不建议在类外创建实例变量
# jian_ning = Person()
# jian_ning.name = "建宁"
# print(jian_ning.name)


# class Person:
#     def set_name(self,name):
#         self.name = name
#
# # 不建议在__init__外创建实例变量
# jian_ning = Person()
# jian_ning.set_name("建宁")
# print(jian_ning.name)
