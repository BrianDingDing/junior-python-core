"""
    数据库基本操作
"""
import pymysql

"""
功能: 连接数据库
host: 主机地址; 本地或localhost.
port: 端口号, 默认3306.
user: 用户名
password: 密码
database: 库
charset: 编码方式, 推荐使用utf8.

P.S 1 必须使用关键字传参.
P.S 2  连接本机库可以不写host和port.
"""
db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="junior_python_core",
    charset="utf8"
)

"""
cur = db.cursor() 
功能: 创建游标.
返回值: 返回游标对象, 用于执行具体SQL命令得到执行结果集的对象.
"""
cur = db.cursor()

"""
cur.execute(sql,args_list) 
功能执行SQL命令
参数: sql: sql语句
     args_list: 列表, 用于给sql语句传递参量.
"""
"""
db.commit() 提交到数据库执行, 必须支持事务操作才有效.
db.rollback() 回到原来的数据形态, 必须支持事务操作才有效.
"""
# 数据库读写操作
# 通过程序操作数据库自动开启事务, 如果数据表不支持事务则执行语句后立即生效; 支持事务的话, 需要提交和回滚处理.
try:
    sql = "INSERT INTO pymysql_demo01 VALUES(2, 'bb');"
    cur.execute(sql)
    db.commit()  # 事务提交
except Exception as e:
    print(e)
    db.rollback()  # 事务回滚

"""
cur.close() 关闭游标对象.
db.close() 关闭数据库连接.
"""
cur.close()
db.close()
