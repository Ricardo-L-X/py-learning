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



