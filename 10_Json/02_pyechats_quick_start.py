from pyecharts.charts import Line
from pyecharts.options import TitleOpts

line = Line()
# 设置x轴
line.add_xaxis(["CN","US","JP"])
# 设置y轴
line.add_yaxis("GDP",[30,20,10])

# 参数配置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示")
)

line.render()