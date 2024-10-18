"""
    SQL注入攻击: 输入数据时, 故意输入sql语句, 当sql语句一旦在后端执行破坏其数据库.
"""
import pymysql

db = pymysql.connect(
    user="root",
    password="root",
    database="junior_python_core",
    charset="utf8"
)

cur = db.cursor()

try:
    id = input('请输入删除的id>>')

    # 输入了 9 or 1=1, 就会导致全表数据删除.
    # sql = f"delete from test where id = {id}"
    # cur.execute(sql)

    # 用%s占位符接收列表传入的值.
    sql = "DELETE FROM pymysql_demo01 WHERE id = %s"
    # 给sql传递数值 -> 不能传递字段名, 表名和运算符.
    # 防止SQL注入攻击.
    cur.execute(sql, [id])

    db.commit()
except Exception as e:
    print(e)
    db.rollback()
