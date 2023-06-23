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


