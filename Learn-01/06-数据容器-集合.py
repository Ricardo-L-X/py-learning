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

print("------------------------------------------------")
# Example 信息去重
my_list = ['glj', 'ymy', 'wxw', 'cqx', 'tmn', 'tj', 'tj', 'ymy','wxw']

my_set = set()
for i in my_list:
    my_set.add(i)

my_list.clear()
for i in my_set:
    my_list.append(i)
print(my_list)