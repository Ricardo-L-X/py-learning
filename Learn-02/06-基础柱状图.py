from pyecharts.charts import Bar
from pyecharts.options import *

my_bar = Bar()

my_bar.add_xaxis(["中国", "日本", "印度"])
my_bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(
    position="right"
)) # 这个就是把目标数据对应在右侧

# 反转 x，y轴
my_bar.reversal_axis()

my_bar.render("基础柱状图.html")