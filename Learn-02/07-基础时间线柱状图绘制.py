from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

'''
    时间线柱状图的本质是按照时间线去显示图标，
    就是添加一个时间线对象，然后若干个时间点的图表，将这若干个时间线图表都添加进去
'''
# 图表1
my_bar1 = Bar()
my_bar1.add_xaxis(["中国", "日本", "印度"])
my_bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(
    position="right"
))
my_bar1.reversal_axis()

# 图表2
my_bar2 = Bar()
my_bar2.add_xaxis(["中国", "日本", "印度"])
my_bar2.add_yaxis("GDP", [10, 20, 30], label_opts=LabelOpts(
    position="right"
))
my_bar2.reversal_axis()

# 添加到时间线
my_timeline = Timeline(
    {"theme": ThemeType.LIGHT}  # 扔一个颜色设置进去，可以更改主题
)

my_timeline.add(my_bar1, "2021年GDP")
my_timeline.add(my_bar2, "2022年GDP")

# 进行一些设置
my_timeline.add_schema(
    play_interval=1000,     # 自动播放的时间间隔
    is_timeline_show=True,  # 是否在自动播放时显示时间线
    is_auto_play=True,      # 是否自动播放
    is_loop_play=True       # 是否循环自动播放
)

my_timeline.render("基础柱状图-时间线.html")