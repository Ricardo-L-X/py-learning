

# Python-Learning

## Python基础学习

### 01-random

money-case

```python
import random

money=10000

for i in range(1, 21):
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}的绩效分为{score}, 下一位")
        continue

    if money >= 1000:
        money -= 1000
        print(f"员工{i}工资为1000, 余额{money}")
    else:
        print("余额不足")
```



### 02-none

None-case

```python
def check_age(age):
    if age < 18:
        return None
    else:
        return "SUCCESS"

result = check_age(16)
if not result:
    print("未成年!")
```



### 03-input

ATM-case

```python
total_money = 50000

def check():
    print(f"余额{total_money}")

def save(temp):
    global total_money  # 这个有点特殊 全局变量 total_money 不能直接在函数中更改，不会生效，得用 global 修饰一下，变得可改
    total_money += temp
    print(f"余额{total_money}")

def get(temp):
    global total_money
    total_money-=temp
    print(f"余额{total_money}")


def main():
    print("-------------------------------")
    print("查询金额\t\t[op1]")
    print("存款\t\t[op2]")
    print("取款\t\t[op3]")

    return input("请输入你想进行的操作：") # 注意一下 input 的输入是字符串，要是要用数字得类型转换 int

while True:
    option = main()
    if(option == "1"):
        check()
    elif(option == "2"):
        temp = int(input("存款金额？"))
        save(temp)
    else:
        temp = int(input("取款金额？"))
        get(temp)


```



### 04-数据容器-列表list

```python
my_list = ['python', 777, [1,2,3]]
print(my_list) # 可以原封不动打印
print(my_list[-1]) # 打印最后一个元素

'''
    insert(int, 'text')
    append('text')
    extend(list)
    clear()
    del my_list(i)
    pop(i)
    remove('text')
    count
    len
    index('text')
'''
```

### 05-数据容器-元组turple

```python
# 元组不可修改 用（）定义

t1 = (1, "tuple", (3,4,5))
print(t1)
print(t1[-1])
```

### 06-数据容器-集合set

```python
# 集合set是没有顺序的，是无序列表

set1 = {1, 6, 2, 4, 5, 6} # 1 2 4 5 6 不按照定义顺序，且相同元素无效 且不支持下标访问
set2 = {1, 5, 6}
print(set1)

# 1、空集合
my_set = set()
print(my_set)
my_set = set1
print(my_set)

print("------------------------------------------------------")

# 但是集合允许修改
# 2、add
my_set.add(333) # 333
my_set.add(333) # 无效
print(my_set)
print(set1)  # 奇了怪了 my_set = set1 竟然是引用传参 修改 my_set 也连带修改 set1

# 3、remove
my_set.remove(6)
print(my_set)

# 4、随机丢出pop
element = my_set.pop() # 不支持指定元素
print(element)
print(my_set)

# 5、clear()
my_set.clear()
print(my_set)

print("--------------------------------------------")

# 6、difference 差集 集合1 有 集合2 没有
set1 = {4, 5, 6}
set2 = {4, 5, 8}
set3 = set1.difference(set2) # 得到新集合而原集合不变
print(set1)
print(set2)
print(set3)

# 7、difference_update 消除差集，就是把 set1 中 set2 有的去掉
set1.difference_update(set2)
print(set1) # 6

# 8、集合合并 union
set4 = set1.union(set2)
print(set4)

# 9、元素个数 （注意，集合自动去重）
set1 = {1,2,3,4,5,1,2,3,4,5}
length = len(set1)
print(length)

# 10、遍历，不支持下标，用for
for i in set1:
    print(i, end=" ")
```

小案例

```python
# Example 信息去重
my_list = ['glj', 'ymy', 'wxw', 'cqx', 'tmn', 'tj', 'tj', 'ymy','wxw']

my_set = set()
for i in my_list:
    my_set.add(i)

my_list.clear()
for i in my_set:
    my_list.append(i)
print(my_list)
```

### 07-数据容器-字典

#### 7.1-字典的定义

```python
# 1、定义
my_dict = {"001":"glj", "002":"ymy", "003":"wxw"}
print(my_dict)

# 2、定义 空
dict1 = {}
dict2 = dict()

# 3、字典不允许重复，后面的会覆盖前面的
dict1 = {"001":"glj", "001":"ymy"}
print(dict1)

# 4、取元素
name = my_dict["001"]
print(f"001号是{name}")

# 5、字典嵌套 可以搞出一个列表，相当于二维数组
stu_score_dict = {
    "glj":{
        "语文":99,
        "数学":100,
        "英语":80
    },
    "ymy":{
        "语文":80,
        "数学":10,
        "英语":8
    },
    "wxw":{
        "语文":9,
        "数学":1,
        "英语":80
    }
}
print(stu_score_dict)
score = stu_score_dict['ymy']['英语'] # 类似于二维数组的表示
print(score)
```

#### 7.2-字典的操作

```python
# 6、修改和新增
my_dict["004"] = 'tj' # 新增
print(my_dict)
my_dict["004"] = 'tmn' # 修改
print(my_dict)

# 7、删除
my_dict.pop("004") # 直接打key就行
print(my_dict)

# 8、清除 clear
my_dict2 = stu_score_dict
print(my_dict2)

# 9、获取全部key
keys = my_dict.keys()
print(keys)

# 10、遍历
for key in my_dict:
    print(f"{key}:{my_dict[key]}")
```

### 08-匿名函数

```python
# 1、函数作为参数传递
def func_test(compile):  # 多此一举
    result = compile(1, 2)   # 对1，2执行compile功能，但是不管compile功能具体是什么
    return result

def compile(x, y):
    return x+y

print(func_test(compile)) # 多此一举


# 2、lambda关键字，匿名函数
print(func_test(lambda x, y: x - y)) # 就是直接把 compile 的实现写在调用里面
```

### 09-文件操作

```python
#三种模式 r 只读；w 重写或创建；a 追加或创建

# 1、r
f = open("test-01.txt", "r", encoding="UTF-8")
print(f.read(2))
print(f.read(10))
print("----------------")
print(f.read(10))

# 注意：连续调用read的时候，下一次read的开始位置是上一次read的结束位置

print("--------------------------------------------")
f2 = open("test-01.txt", "r", encoding="UTF-8")
print(f2.readline())  # 只读一行

f3 = open("test-01.txt", "r", encoding="UTF-8")
print(f3.readlines())  # 全部读完

# with open 语句
print('with open:')
with open("test-01.txt", "r", encoding="UTF-8") as f4:
    print(f4.readlines())


# 2、w 文件不存在就创建，文件存在就清空原有内容然后重写
with open("test-02.txt", "w", encoding="UTF-8") as f5:
    f5.write("爱情来的太快就像龙卷风\n离不开暴风圈来不及逃\n")
    f5.flush() # 刷新一下，从内存转存到硬盘


# 3、a 文件不存在就创建，文件存在就追加
with open("test-02.txt", "a", encoding="UTF-8") as f6:
    f6.write("我不能再想\n我不能再想\n")
    f6.flush() # 刷新一下，从内存转存到硬盘
    

# 4、文件综合操作案例
f_read = open("test-03-bill.txt", "r", encoding="UTF-8")
f_write = open("test-04-bill.txt","w",encoding="UTF-8")
for line in f_read:
    line = line.strip()   # 字符串的 strip 函数，将首尾的空格、换行符等去掉
    if line.split(",")[4] == "测试":   # 字符串 split 函数，就是按照 split 中的元素进行分割，并将分割出的元素装在列表中返回
                                        # 有点不大理解，原文如果把逗号换成中文逗号，这里的split里面无论是中文逗号还是英文逗号都报错
        continue
    f_write.write(line)
    f_write.write("\n")

f_read.close()
f_write.close()
```

### 10-python模块

首先是自定义一个，类似于一个功能类

```python
# 这是一个自定义模块，用来专门写函数
def Add(x, y):
    return x + y


if __name__ == '__main__':   # main 是py的一个内置变量，只有在本文件中run时才会执行其中的操作 在调用文件中 run 时不会执行
    print(Add(4,6))
```

再调用

```python
import my_module as mm

print(mm.Add(3, 3))
```



## Python-Pyecharts

### 01-json文件及格式转换

```python
import json

# json文件的格式本质上就是字典，或者说是列表嵌套字典

# 1、准备列表，将列表转换为json
data = [{
    "name":"glj",
    "age":11,
}, {
    "name":"ymy",
    "age":20,
}, {
    "name":"wxw",
    "age":"18",
}]

json_str = json.dumps(data, ensure_ascii=False) # 通过这个内置函数，转换为 json文件   如果有中文，想要正确显示，就设置 ensure_ascii 参数为 false
print(json_str)


# 2、准备字典，将字典转换为 json
data2 = {"name":"glj", "age":11}
json_str2 = json.dumps(data2, ensure_ascii=False)
print(json_str2)

# 3、将 json 字符串转换为 列表
js = '[{"name":"glj", "age":11}, {"name":"ymy", "age":20}, {"name":"wxw","age":"18"}]'
data3 = json.loads(js)
print(data3)


```

### 02-pyecharts基础入门

#### 2.1 简单折线图

```python
# 导包
from pyecharts.charts import Line
# 创建一个新的折线图对象
my_line = Line()
# 给折线图对象添加x轴数据
my_line.add_xaxis(["中国", "美国", "英国"])
# 给折线图对象添加y轴数据
my_line.add_yaxis("GDP", [30, 20, 10]) # 30 20 10 分别对应x轴三项
# 通过 render 将代码变成图像
my_line.render()
```

![image-20230621214347118](C:\Users\Ricardo\AppData\Roaming\Typora\typora-user-images\image-20230621214347118.png)

#### 2.2 加入全局配置

```python
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
```

![image-20230621215536848](C:\Users\Ricardo\AppData\Roaming\Typora\typora-user-images\image-20230621215536848.png)

### 03-折线图开发

**整个过程分为两个部分，第一部分是读取json文件数据并进行预处理成字典；第二部分是从字典提取有效的x和y来进行绘图**

第一部分

```python
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
```

第二部分

```python
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
```

![image-20230622003946650](C:\Users\Ricardo\AppData\Roaming\Typora\typora-user-images\image-20230622003946650.png)

### 04-全国地图可视化

#### 4.1 普通版本

```python
from pyecharts.charts import Map

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

my_map.render()
```

#### 4.2 让地图更丰富，配置全局选项

```python
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
my_map = Map()
# 准备数据
# 地图数据的形式，就是元组的列表，一对一
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
```

![](C:\Users\Ricardo\AppData\Roaming\Typora\typora-user-images\image-20230623120509768.png)

### 05 省级疫情地图可视化

```python
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
```

![image-20230623120627114](C:\Users\Ricardo\AppData\Roaming\Typora\typora-user-images\image-20230623120627114.png)

### 06-基础柱状图

```python
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
```

![image-20230623120652700](C:\Users\Ricardo\AppData\Roaming\Typora\typora-user-images\image-20230623120652700.png)

### 07-基础柱状图——时间线

```python
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
```

![image-20230623120713740](C:\Users\Ricardo\AppData\Roaming\Typora\typora-user-images\image-20230623120713740.png)

### 08-动态时间线柱状图

1、列表的sort方法并配合lambda匿名函数完成列表排序

*列表**.sort(key =* *选择排序依据的函数**, reverse=True/False) True* *表示反转 降序**
**key**：要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的一句**
**reverse**：是否反转排序结果

```python
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
```

2、完成图表所需的数据处理

```python
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
```

3、完成GDP动态图表绘制

```python
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
```

![image-20230623120737943](C:\Users\Ricardo\AppData\Roaming\Typora\typora-user-images\image-20230623120737943.png)

## Python-PySpark













## Python-Django

### 01-创建

1. 删掉**templates**这个文件夹
2. 找到与工程名字相同的文件夹，在 **settings.py** 这个文件中，第58行，删掉 ‘DIRS’ 中的内容然后保存
3. 在工程文件的，命令行中输入命令：

```python
python3.10 manage.py startapp app01
```

​		这样就创建了一个app文件夹，也就是app功能块，所有的操作都在app里面进行

> app01文件夹的结构，只有models.py（对数据库进行操作）和views.py（函数）是需要操作的，其他不用管

4. 在与工程文件名相同的文件夹中，找到**settings.py**文件，在33行的 **INSTALLED_APPS**列表中，加入自己刚刚创建的APP，代码为：

```python
'app01.apps.App01Config'
```

5. 编写URL和视图函数的对应关系，在**urls.py**文件中

```python
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', views.index)
]
```

6. 编写视图函数，在**app01**文件夹的**views.py**文件中

```python
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(s'欢迎使用')
```

7. 启动Django程序

​	点击右上角的绿色启动按钮，就会 run django工程，而不能在页面点run，那样只是run文件

**当然，可以重复上面的5-7步骤，即可创建多个对应的URL和视图函数**

### 02-templates

用于存放HTML文件，此时的views文件中就要返回如下：

```python
def user_html(request):
    return render(request, 'test01.html') # 默认在本 app 下面的 templates 目录里面去寻找
```

相应的，这个我们编写的html文件要放在app01文件夹下面新创建的templates文件夹中

### 03-static

- 图片

- css

- js

- plugins

  这些都会被当作是静态文件，都放在app01文件夹下新创的static文件夹下的css、img、js、plugins文件夹中

  

## Python-DeepLearning

### FacialRecognition

#### 01-读取图片

```python
import cv2 as cv

# 读取图片
img = cv.imread('1.jpg')

# 显示图片
cv.imshow('read_img', img)

# 等待
cv.waitKey(10000) # 图片显示10000ms

# 释放内存
cv.destroyAllWindows()
```

#### 02-灰度转换

```python
import cv2 as cv

# 读取图片
img = cv.imread('1.jpg')


# 灰度转换
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 显示灰度
cv.imshow('gray', gray_img)
# 保存灰度图片
cv.imwrite('gray_face1.jpg', gray_img)


# 显示图片
cv.imshow('read_img', img)

# 等待
cv.waitKey(5000) # 图片显示5000ms

# 释放内存
cv.destroyAllWindows()
```

#### 03-修改尺寸

```python
import cv2 as cv

# 读取图片
img = cv.imread('1.jpg')

# 修改尺寸
resize_img = cv.resize(img, dsize=(200, 200))

# 显示原图
cv.imshow('img', img)

# 显示修改后的
cv.imshow('resize_img', resize_img)

# 打印原图尺寸
print('未修改：', img.shape)

# 打印修改后的原图尺寸
print('修改：', resize_img.shape)

# 等待
while True:
    if ord('q') == cv.waitKey(0):
        break

# 释放内存
cv.destroyAllWindows()
```

#### 04-绘制矩形

```python
import cv2 as cv

# 读取图片
img = cv.imread('1.jpg')

# 坐标
x,y,w,h = 100, 100, 100, 100

# 绘制矩形
cv.rectangle(img, (x, y, x+w, y+h), color=(0, 0, 255), thickness=1)

# 绘制圆形
cv.circle(img, center=(x+w, y+h), radius=100, color=(255, 0, 0), thickness=5)

# 显示
cv.imshow('re_img', img)


# 等待
while True:
    if ord('q') == cv.waitKey(0):  # 按下q键，退出图片显示
        break

# 释放内存
cv.destroyAllWindows()
```

#### 05-人脸检测

```python
import cv2 as cv

# 建立检测函数
def face_detect_demo(img):
    # 先把图片灰度化
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 调取分类器
    face_detect = cv.CascadeClassifier('/Users/ricardo/anaconda3/envs/testNew-01/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(image=gray,
                                        scaleFactor=1.01, # 这个值需要不断调整，如果没有调到适合值，可能会误触
                                        minNeighbors=5,
                                        flags=0,
                                        #minSize=(100, 100), # 人脸最小，100*100的框中不可能有人脸 可不填
                                        #maxSize=(1000, 1000) # 人脸最大，1000*1000的框外不可能有人脸 可不填
                                        )
    '''
        detectMultiScale函数的几个参数是 灰度图像 每次缩放倍数 每次检测5次这里都有人脸后才算数 
    '''
    for x,y,w,h in face:
        # 在原图上画矩形，把人脸框出来
        cv.rectangle(img, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img)

# 读取图片
img = cv.imread('data/exist/4.jjy.jpg')
# 检测函数
face_detect_demo(img)
# 等待
while True:
    if ord('q') == cv.waitKey(0):  # 按下q键，退出图片显示
        break

# 释放内存
cv.destroyAllWindows()
```

#### 06-检测多个

```python
import cv2 as cv

# 建立检测函数
def face_detect_demo(img):
    # 先把图片灰度化
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 调取分类器
    face_detect = cv.CascadeClassifier('/Users/ricardo/anaconda3/envs/testNew-01/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(image=gray,
                                        scaleFactor=1.075, # 这个值需要不断调整，如果没有调到适合值，可能会误触 1.07
                                        minNeighbors=5,
                                        flags=0,
                                        minSize=(70, 70), # 人脸最小，100*100的框中不可能有人脸 可不填
                                        maxSize=(100, 100)) # 人脸最大，1000*1000的框外不可能有人脸 可不填
    '''
        detectMultiScale函数的几个参数是 灰度图像 每次缩放倍数 每次检测5次这里都有人脸后才算数 不管 最小范围 最大范围
    '''
    for x,y,w,h in face:
        # 在原图上画矩形，把人脸框出来
        cv.rectangle(img, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img)

# 读取图片
img = cv.imread('2.jpg')

# 检测函数
face_detect_demo(img)

# 等待
while True:
    if ord('q') == cv.waitKey(0):  # 按下q键，退出图片显示
        break

# 释放内存
cv.destroyAllWindows()
```

单个的人脸检测和多个的人脸检测没有任何区别，只是把图片换一下

需要注意的是，为了同时识别到多个人脸，分类器 `face_detect` 的 `detectMultiScale` 函数中，`scaleFactor`参数需要不断调整，直至能够识别到所有的人脸，并且不出现其他的误识别

#### 07-视频检测

```python
import cv2 as cv

# 建立检测函数
def face_detect_demo(img):
    # 先把图片灰度化
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 调取分类器
    face_detect = cv.CascadeClassifier('/Users/ricardo/anaconda3/envs/testNew-01/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(image=gray,
                                        scaleFactor=1.075, # 这个值需要不断调整，如果没有调到适合值，可能会误触 1.07
                                        minNeighbors=5,
                                        flags=0,
                                        minSize=(70, 70), # 人脸最小，100*100的框中不可能有人脸 可不填
                                        maxSize=(100, 100)) # 人脸最大，1000*1000的框外不可能有人脸 可不填
    '''
        detectMultiScale函数的几个参数是 灰度图像 每次缩放倍数 每次检测5次这里都有人脸后才算数 不管 最小范围 最大范围
    '''
    for x,y,w,h in face:
        # 在原图上画矩形，把人脸框出来
        cv.rectangle(img, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=2)
    cv.imshow('result', img)

# 读取视频
# cap = cv.VideoCapture(0)
cap = cv.VideoCapture("") # 填写视频路径

while True:
    flag, frame = cap.read() # 播放标记 帧
    # 如果播放完毕
    if not flag:
        break
    # 检测函数
    face_detect_demo(frame)
    # 等待
    if ord("q") == cv.waitKey(0):
        break


# 释放内存
cv.destroyAllWindows()
#释放摄像头
cap.release()
```

#### 08-信息保存

```python
# 导入模块
import cv2 as cv

cap = cv.VideoCapture(0)

flag = 1
num = 1

while(cap.isOpened()):
    # 得到每帧图像
    ret_flag, Vshow = cap.read()
    # 显示图像
    cv.imshow("Capture_test", Vshow)
    # 按键判断
    while True:
        if ord("s") == cv.waitKey(1):
            cv.imwrite("/Users/ricardo/Desktop/PythonProject/FacialRecognition/opencv/data/save/"+str(num)+"-name"+".jpg", Vshow)  # name 是人的名字
            print("success to save"+str(num)+".jpg")
            print("------------------------------------")
            num+=1
        elif cv.waitKey(1) == ord(" "):   # 退出
            break


cap.release()

cv.destroyAllWindows()
```

#### 09-数据训练

```python
import os
import cv2 as cv
from PIL import Image
import numpy as np


def getImageAndLabels(path):
    # 储存人脸数据
    facesSamples = []
    # 储存名字
    ids = []
    # 储存图片信息
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # 加载分类器
    face_detector = cv.CascadeClassifier(
        '/Users/ricardo/anaconda3/envs/testNew-01/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    # 遍历图片
    for imagePath in imagePaths:
        # 打开图片，灰度化 PIL
        '''
            PIL有九种不同模式：1(黑白）,L（灰度）,P,RGB,RGBA,CMYK,YCbCr,I,F
        '''
        PIL_img = Image.open(imagePath).convert('L')
        # 将图像转化为数组，黑白的深浅
        '''
            转换成灰度后，就可以用0-255数字来表示，这样就相当于向量化，存到 img_numpy 数组中，表示的就是一整张图片
        '''
        img_numpy = np.array(PIL_img, 'uint8')
        # 获取图片人脸特征
        '''
            把一整张图片的人脸的那一部分框起来
        '''
        faces = face_detector.detectMultiScale(img_numpy)
        # 获取每张图片的id和姓名
        id = int(os.path.split(imagePath)[1].split('.')[0])  # 看命名，如果是1-jjy就用-分隔
        # 预防无面容的照片
        '''
            这就是把人的id和脸部特征对应起来，同一个下标下的两个数组 ids 和 facesSamples 元素就是对应起来的
        '''
        for x, y, w, h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y + h, x:x + w])
        # 打印脸部特征和id
        print("id: ", id)
        print("fs: ", facesSamples)
    return facesSamples, ids


if __name__ == '__main__':
    # 图片路径
    path = './data/exist/'
    # 读取图像数组和id标签数组和签名
    faces, ids = getImageAndLabels(path)
    # 加载识别器
    recognizer = cv.face.LBPHFaceRecognizer_create()
    # 训练，将身份信息和图片整合
    recognizer.train(faces, np.array(ids))
    # 保存文件
    recognizer.write('trainer/trainer.yml') # 这里一定要建立一个trainer文件夹，不然报错，找不到路径
```

#### 10-人脸识别

```python
import os
import cv2 as cv
import urllib
import urllib.request

# 加载训练数据文件
recognizer = cv.face.LBPHFaceRecognizer_create()
# 加载数据
recognizer.read('./trainer/trainer.yml')

# 名称
names=['jjy']
# 警报全局变量
warningtime = 0
# md5加密
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode('utf8'))
    return m.hexdigest()   # 就是对密码进行一个加密
# 短信反馈
statusStr = {
    '0': '短信发送成功',
    '-1': '参数不全',
    '-2': '服务器空间不支持，请确认支持url或者fsocket，联系客服解决',
    '30':'密码错误',
    '40':'账号不存在',
    '41':'余额不足',
    '42':'账户已过期',
    '43':'IP地址限制',
    '50':'内容有敏感词'
}
# 报警模块
def warning():
    smsapi = "http://api.smsbao.com/"
    # 短信平台账号
    user = '17786661838'
    # 短信平台密码
    password = md5('123456')
    # 要发送信息
    content = '【报警】\n原因：xxx\n地点：xxx\n时间：xxx'
    # 要发送短信的手机号码
    phone = '17786661838'

    data = urllib.parse.urlencode({'u': user, 'p': password, 'm': phone, 'c': content})
    send_url = smsapi + 'sms?' + data
    response = urllib.request.urlopen(send_url)
    the_page = response.read().decode('utf-8')
    print(statusStr[the_page])

# 准备识别的图片
def face_detect_demo(img):
    # 灰度化
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 调取分类器
    face_detector = cv.CascadeClassifier('/Users/ricardo/anaconda3/envs/testNew-01/lib/python3.8/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
    # 识别出正确范围的人脸
    face = face_detector.detectMultiScale(
        image = gray,
        scaleFactor=1.1,
        minNeighbors=5,
        flags=0,
    )
    # 对于识别出的人脸，给人脸画框框
    for x,y,w,h in face:
        # 画方框
        cv.rectangle(img, (x, y), (x+w, y+h), color=(0,0,255), thickness=2)
        # 画圆框
        cv.circle(img, center=(x+w//2, y+h//2), radius=w//2, color=(0, 255, 0), thickness=2)
        # 人脸识别
        ids, confidences = recognizer.predict(gray[y:y+h, x:x+w])
        print('标签id：', ids, '置信评分：', confidences)
        # 判断
        if confidences > 80:  # 如果置信评分超过了80这个界限，则爸警报变量+1
            global warningtime
            warningtime += 1
            if warningtime > 100:  # 一旦警报变量超过了100，则认定为陌生人，发出警报
                warning()
                warningtime = 0
            cv.putText(img, 'unknow', (x+10, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 1)
        else:
            cv.putText(img, str(names[ids-1]), (x+10,y-10),cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 1)
    cv.imshow('result:', img)

if __name__ == '__main__':
    # 读取图片
    # img = cv.imread('data/exist/1.jjy.jpg')
    img = cv.imread('./data/exist/1.jjy.jpg')
    # 进行检测
    face_detect_demo(img)
    # 等待
    while True:
        if ord('q') == cv.waitKey(0):
            break
    # 释放内存
    cv.destroyAllWindows()
```

**现在有一个 bug 就是，不知道为什么 names 名字列表是空的，忘了是在哪里将名字填入名字列表的了。导致只有识别第一张图片（id=1）时，才能识别成功。**
