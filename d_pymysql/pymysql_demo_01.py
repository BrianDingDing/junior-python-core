"""
    数据库操作
"""
import pymysql

# 连接数据库, 连接本机库可以不写host, port
db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="cycle",
    charset="utf8"
)

# 生成一个游标: 用于调用SQL语句得到执行结果集的对象
cur = db.cursor()

# 数据库读写操作
# 通过程序操作数据库自动开启事务, 如果数据表不支持事务则执行语句后立即生效, 支持事务的话, 需要提交和回滚处理.
try:
    sql = "insert into test values(2, 'bb');"
    cur.execute(sql)
    db.commit()  # 事务提交
except Exception as e:
    print(e)
    db.rollback()  # 事务回滚

# 关闭游标和数据库连接
cur.close()
db.close()
