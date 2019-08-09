#函数def=define
def func1():
    print("hello function~")

def sum(a,b):
    print(a+b)


#return return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
def func2():
    return "this is the result of func2"
a=func2()

def sum2(a,b,c):
    return a*b*c
print(sum2(2,3,4))
