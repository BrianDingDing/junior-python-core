"""
    批量执行SQL语句
"""
import pymysql

db = pymysql.connect(
    user="root",
    password="root",
    database="cycle",
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

try:
    sql = "insert into test values(%s, %s);"
    # 多次执行SQL语句
    cur.executemany(sql, data)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
