#converter函数是可定义变量的
def converter(weight):
    ponds=weight/0.45
    print(ponds)

converter(60)
#converter2函数是变量是个定值
def converter2(weight=100):
    ponds=weight/0.45
    print(ponds)

converter2()