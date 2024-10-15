"""
    数据库读操作
"""
import pymysql

db = pymysql.connect(
    user="root",
    password="root",
    database="cycle",
    charset="utf8"
)

cur = db.cursor()

try:
    sql = "select * from test;"
    cur.execute(sql)

    # # 迭代游标获取查询结果
    # # 每条查询结果只能取一次
    # for row in cur:
    #     print(row)

    # one = cur.fetchone()
    # print("one:", one)
    #
    # many = cur.fetchmany(2)
    # print("many:", many)

    all = cur.fetchall()
    print("all:", all)

except Exception as e:
    print(e)
