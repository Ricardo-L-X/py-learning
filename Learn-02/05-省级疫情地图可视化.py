import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

f = open("疫情.txt", "r", encoding="UTF-8")
data = f.read()

f.close()

data_dict = json.loads(data)

# 取出将要使用的数据
cities_data = data_dict["areaTree"][0]["children"][3]["children"]

# 准备数据为元组并放入list
data_list = []
for city_data in cities_data:
    city_name = city_data["name"] + "市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

# 手动添加济源市的数据
data_list.append(("济源市", 5))
print(data_list)

# 构建地图
my_map = Map()
# 添加数据
my_map.add("河南省疫情分布", data_list, "河南")

# 配置全局选项
my_map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1, "max":9, "label": "1-9人", "color":"#CCFFFF"},
            {"min":10, "max":99, "label": "10-99人", "color":"#FF6666"},
            {"min":100, "max":999, "label": "100-999人", "color":"#990033"},
            {"min":1000, "max":9999, "label": "1000-9999人", "color":"#CCFFFF"},
            {"min":10000, "max":99999, "label": "10000-99999人", "color":"#CCFFFF"},
        ]
    )
)


# 画图
my_map.render("河南省疫情地图.html")
