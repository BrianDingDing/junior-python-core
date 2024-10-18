"""
    批量执行SQL语句
"""
import pymysql

db = pymysql.connect(
    user="root",
    password="root",
    database="junior_python_core",
    charset="utf8"
)

cur = db.cursor()

# 准备数据
data = [
    (1, "aa"),
    (2, "bb"),
    (3, "cc"),
    (4, "dd")
]

"""
cur.executemany(sql, args_list)
功能: 多次执行SQL命令, 执行次数由列表中元组数量决定.
参数： sql: sql语句
      args_list: 列表中包含元组, 每个元组用于给sql语句传递参量, 一般用于写操作.
"""
try:
    sql = "INSERT INTO pymysql_demo01 VALUES(%s, %s);"
    # 多次执行SQL语句
    cur.executemany(sql, data)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
