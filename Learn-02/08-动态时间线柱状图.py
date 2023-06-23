from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 1、列表的sort方法并配合lambda匿名函数完成列表排序
'''
    列表.sort(key = 选择排序依据的函数, reverse=True/False) True 表示反转 降序
    key：要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的一句
    reverse：是否反转排序结果
'''
my_list = [['a', 33], ['b', 11], ['c', 55]]
# 有名函数
def choose_sort_key(element):
    return element[1]
my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)

# 匿名函数
my_list.sort(key = lambda element: element[1], reverse=False)
print(my_list)


# 2、完成图表所需的数据处理
f_gdp = open("1960-2019全球GDP数据.csv", "r", encoding="GBK")
data_lines = f_gdp.readlines()
f_gdp.close()
data_lines.pop(0) # 删除列表的第一行数据

# 处理成字典
dict_data={}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])

    # 如果year存在，则把现有列表取出来；如果year不存在，则添加列表
    try:
        dict_data[year].append([country, gdp])   # 如果 year 存在，则不报错
    except KeyError:
        dict_data[year] = []                     # 如果 year 不存在，则创建
        dict_data[year].append([country, gdp])   # 添加数据


# 对列表元素按照 GDP 排序
#  注意 for 循环的时候不要直接去循环字典，因为这样顺序可能会打乱，因此我们先把 key 取出来，然后再按照 key 排序
# 首先取出全部的key
keys = dict_data.keys()
sorted_year_list = sorted(keys)
print(sorted_year_list)


# 3、完成GDP动态图表绘制
# for-loop
# 时间线 注意一下啊 时间线的对象一定要设置在 for 循环的外面
my_timeline = Timeline(
    {"theme": ThemeType.LIGHT}
)
for year in sorted_year_list:
    # 排序并取出前八个
    dict_data[year].sort(key=lambda element: element[1], reverse=True)
    year_data = dict_data[year][0:8]
    print(year_data)
    x_data = []
    y_data = []
    for every in year_data:
        x_data.append(every[0])
        y_data.append(every[1] / 100000000)

    # 这里有一个小问题，就是反转后会发现坐标轴的排序是按照 最多的在最下面，最少的在最上面。因此这里横纵坐标还需要再反转一下
    x_data.reverse()
    y_data.reverse()
    # 导入数据
    my_bar = Bar()
    my_bar.add_xaxis(x_data)
    my_bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(
        position="right"
    ))
    my_bar.reversal_axis()
    # 设置标题
    my_bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年的前八GDP数据")
    )

    my_timeline.add(my_bar, str(year))


my_timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
my_timeline.render("1960-2019全球GDP数据.html")

