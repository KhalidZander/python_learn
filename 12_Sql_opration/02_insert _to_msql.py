from data_loader import *
from pymysql import Connection

csv_path = "./11_Class/数据分析案例/data.txt"

json_path = "./11_Class/数据分析案例/data.json"

csv = CsvDataLoader(csv_path)

jan_data= csv.read_data()

json =JsonDataLoader(json_path)

feb_data=json.read_data()

all_data:list[Data] = jan_data +feb_data


conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True, # 可选 是否自动提交插入
)

cursor = conn.cursor()

conn.select_db("my_database1")

for record in all_data:
    sql = f"insert into orders values('{record.date}','{record.order_id}',{record.money},'{record.province}')"
    cursor.execute(sql)
    print(sql)

# 从数据库中获取order数据并大于



conn.close()
    