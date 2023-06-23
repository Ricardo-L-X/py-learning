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

print("--------------------------------------------------------------")

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

