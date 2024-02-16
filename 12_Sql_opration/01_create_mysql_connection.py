from pymysql import Connection

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
cursor.execute("select * from student")
# 通过fetchall获取数据 数据类型是嵌套的元组
res = cursor.fetchall()

for data in res:
    print(data)


# 插入数据

cursor.execute("insert into student values(110,'周润发',19,'男')")

conn.close()