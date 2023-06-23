import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts, LabelOpts

# 1、打开文件
f_us = open("美国.txt", "r", encoding="UTF-8")
f_jp = open("日本.txt", "r", encoding="UTF-8")
f_ind = open("印度.txt", "r", encoding="UTF-8")

# 2、读文件
data_us = f_us.read()
data_jp = f_jp.read()
data_ind = f_ind.read()

# 3、数据预处理
# 3.1、删掉前面的
data_us = data_us.replace("jsonp_1629344292311_69436(", "")
data_jp = data_jp.replace("jsonp_1629350871167_29498(", "")
data_ind = data_ind.replace("jsonp_1629350745930_63180(", "")

# 3.2、删掉后面的
data_us = data_us[:-2]
data_jp = data_jp[:-2]
data_ind = data_ind[:-2]

# 4、转列表or字典
dict_us = json.loads(data_us)
print(dict_us)
dict_jp = json.loads(data_jp)
print(dict_jp)
dict_ind = json.loads(data_ind)
print(dict_ind)

####################################################

# 获取 trend key
trend_data_us = dict_us["data"][0]['trend']
trend_data_jp = dict_jp["data"][0]['trend']
trend_data_ind = dict_ind["data"][0]['trend']
# 获取 x 轴变量——日期   不用全部的数据 取出2022年的314条数据即可
trend_data_us_x = trend_data_us["updateDate"][:314]
trend_data_jp_x = trend_data_jp["updateDate"][:314]
trend_data_ind_x = trend_data_ind["updateDate"][:314]
# 获取 y 轴变量
trend_data_us_y = trend_data_us["list"][0]["data"][:314]
trend_data_jp_y = trend_data_jp["list"][0]["data"][:314]
trend_data_ind_y = trend_data_ind["list"][0]["data"][:314]
print(trend_data_us_x)
print(trend_data_us_y)
print(trend_data_jp_x)
print(trend_data_jp_y)
print(trend_data_ind_x)
print(trend_data_ind_y)
# 画图
my_line = Line()
my_line.add_xaxis(trend_data_us_x) # 横坐标通用
my_line.add_yaxis("美国确诊人数", trend_data_us_y, label_opts=LabelOpts(is_show=False)) # 不显示数据了
my_line.add_yaxis("日本确诊人数", trend_data_jp_y, label_opts=LabelOpts(is_show=False))
my_line.add_yaxis("印度确诊人数", trend_data_ind_y, label_opts=LabelOpts(is_show=False))
# # 设置全局配置项
my_line.set_global_opts(
    title_opts=TitleOpts(title="美、日、印疫情情况展示", pos_left="center", pos_bottom="1%"), # 标题
    legend_opts=LegendOpts(is_show=True), # 图例
    toolbox_opts=ToolboxOpts(is_show=True), # 工具箱
 )

my_line.render()


