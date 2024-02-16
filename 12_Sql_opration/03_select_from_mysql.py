from pymysql import Connection
from data_loader import *

conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True, # 可选 是否自动提交插入
)

print(conn.get_server_info())

# 非查询的sql
#  获取游标对象
cursor = conn.cursor()
#  选择数据库
conn.select_db("my_database1")
#  执行对应的sql查询语句
# cursor.execute("create table test_pymysql(id int);")

# 查询的sql
cursor.execute("select * from orders")
# 通过fetchall获取数据 数据类型是嵌套的元组
res = cursor.fetchall()

all_data:list[Data]=[]

for order in res:
    all_data.append(Data(str(order[0]),str(order[1]),order[2],str(order[3])))

for data in all_data:
    print(data)

conn.close()