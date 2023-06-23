# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 创建一个新的折线图对象
my_line = Line()
# 给折线图对象添加x轴数据
my_line.add_xaxis(["中国", "美国", "英国"])
# 给折线图对象添加y轴数据
my_line.add_yaxis("GDP", [30, 20, 10]) # 30 20 10 分别对应x轴三项

# 设置全局配置项
my_line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"), # 标题
    legend_opts=LegendOpts(is_show=True), # 图例
    toolbox_opts=ToolboxOpts(is_show=True), # 工具箱
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 通过 render 将代码变成图像
my_line.render()