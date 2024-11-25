"""
    数据库读操作
"""
import pymysql

db = pymysql.connect(
    user="root",
    password="root",
    database="junior_python_core",
    charset="utf8"
)

cur = db.cursor()

"""
cur.fetchone() 获取查询结果集的第一条数据, 查找到返回一个元组否则返回None
cur.fetchmany(n) 获取前n条查找到的记录, 返回结果为元组嵌套元组, ((记录1),(记录2)), 查询不到内容返回空元组.
cur.fetchall() 获取所有查找到的记录, 返回结果形式同上.
"""
try:
    sql = "select * from pymysql_demo01;"
    cur.execute(sql)

    # !!!!!每条查询结果只能取一次
    # 第一次查询取一条, 第二个查询就会取后两条, 第三个查询剩下的全部.

    # # 迭代游标获取查询结果
    # for row in cur:
    #     print(row)

    # one = cur.fetchone()
    # print("one:", one)

    # many = cur.fetchmany(2)
    # print("many:", many)

    all = cur.fetchall()
    print("all:", all)

except Exception as e:
    print(e)
