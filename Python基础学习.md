

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
