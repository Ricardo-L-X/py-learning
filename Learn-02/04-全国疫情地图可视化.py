from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
my_map = Map()
# 准备数据
data=[
    ("北京市", 99), # 这个必须要写全，北京市，写北京就不行
    ("上海市", 199),
    ("广东省", 299),
    ("湖南省", 399),
    ("台湾省", 499),
]

my_map.add("测试地图", data, "china")

# 让地图更丰富，配置全局选项
my_map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True, # 开启手动校准
        pieces=[ # 设置具体校准值
            {"min":1, "max":9, "label": "1-9人", "color":"#CCFFFF"},
            {"min":10, "max":99, "label": "10-99人", "color":"#FF6666"},
            {"min":100, "max":999, "label": "100-999人", "color":"#990033"},
            {"min":1000, "max":9999, "label": "1000-9999人", "color":"#CCFFFF"},
            {"min":10000, "max":99999, "label": "10000-99999人", "color":"#CCFFFF"},
        ]
    )
)


my_map.render("全国疫情地图.html")
