#代码报错时，自定义错误输出内容

try:
    print(10/0)

except:
    print("0 cannot be divided~")


#标准的数据
try:
    print(10/8)
    print(10+"0")

except ArithmeticError as e:
    print(e)
except TypeError as t:
    print(t)