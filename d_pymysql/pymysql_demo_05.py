"""
    二进制文件写入与读取
    在数据库中很少存储大的二进制文件, 因为效率低.
"""
import pymysql

db = pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="junior_python_core",
    charset="utf8"
)

cur = db.cursor()

# 二进制文件写入
# try:
#     with open("./static/data.jpeg", "rb") as fr:
#         data = fr.read()
#
#     sql = "UPDATE pymysql_demo01 SET image=%s WHERE id=1;"
#     cur.execute(sql, [data])
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()

# 二进制文件取出
try:
    sql = "SELECT image from pymysql_demo01 WHERE id=1;"
    cur.execute(sql)
    res = cur.fetchone() # (image,)[0]

    with open("./static/new.jpeg", "wb") as fw:
        fw.write(res[0])
except Exception as e:
    print(e)

cur.close()
db.close()
