# 这是一个自定义模块，用来专门写函数
def Add(x, y):
    return x + y


if __name__ == '__main__':   # main 是py的一个内置变量，只有在本文件中run时才会执行其中的操作 在调用文件中 run 时不会执行
    print(Add(4,6))