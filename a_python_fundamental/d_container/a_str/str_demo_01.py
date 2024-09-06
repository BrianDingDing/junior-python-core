"""
    字符串字面值
"""
# 1. 字符串三种写法
data01 = "余纯山"
data02 = '余纯山'
# 可见即所得
data03 = """
余
    纯
山
"""
print(data03)

# 2. 引号冲突
print('我是花果山"水帘洞"美猴王.')
print("我是花果山'水帘洞'美猴王.")
print("""我是"花果山"'水帘洞'美猴王.""")

# 3. 转义符: 改变原始字符的含义
print("我是花果山\"水帘洞\"美猴王.")
print("我是花果山水帘洞\n美猴王.")  # 换行
print("C:\\arogram\\bnternet\\SIGNUP")
print(r"C:\arogram\bnternet\SIGNUP")  # 原始字符

# 4. 格式化字符串
# 占位符: %s: str %.精度f: float %.位数d: decimal
cny = 1234
usd = cny * 0.1438
print("%s人民币=%.2f美元" % (cny, usd))  # 1234人民币=177.45美元
print(f"{cny}人民币={usd:.2f}美元")

minute = 9
second = 0
print("%.2d:%.2d" % (minute, second))  # 09:00
# 整数保留2位, 不足时在前填充0.
print(f"{minute:02}:{second:02}")
