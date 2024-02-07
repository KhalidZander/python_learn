from data_loader import *
from pyecharts.charts import *
from pyecharts.options import *
from pyecharts.globals import *

csv_path = "./11_Class/数据分析案例/data.txt"

json_path = "./11_Class/数据分析案例/data.json"

csv = CsvDataLoader(csv_path)

jan_data= csv.read_data()

json =JsonDataLoader(json_path)

feb_data=json.read_data()

all_data = jan_data +feb_data

data_dic ={}
for data in all_data:
    if data_dic.__contains__(data.date):
        data_dic[data.date]+=data.money
    else:
        data_dic[data.date]=data.money

print(f"每日销售总额如下：\n{data_dic}")

bar = Bar()

bar.add_xaxis(list(data_dic.keys()))
bar.add_yaxis("销售额",list(data_dic.values()))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("./11_Class/数据分析案例/每日销售额柱状图.html")
    