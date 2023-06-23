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

