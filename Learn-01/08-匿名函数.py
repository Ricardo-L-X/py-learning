# 1、函数作为参数传递
def func_test(compile):  # 多此一举
    result = compile(1, 2)   # 对1，2执行compile功能，但是不管compile功能具体是什么
    return result

def compile(x, y):
    return x+y

print(func_test(compile)) # 多此一举


# 2、lambda关键字，匿名函数
print(func_test(lambda x, y: x - y)) # 就是直接把 compile 的实现写在调用里面