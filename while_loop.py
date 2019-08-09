#当con小于10的时候，一直加1，直到con=10,停止并打印con
con = 1
while con<10:
    con = con+1
print(con)

#当n小于10的时候，一直加1并打印，con=10的时候停止打印
n= 1
while n<10:
    n = n+1
    print(n)

#注意以上两个方法的区别

#以下是for_loop循环打印

x = 1
for x in range(1,11):
    print(x)

#while true
while True:
    a = int(input("please enter your age: "))
    b = int(input("please enter your bro's age: "))
    print("SUM a and b = "+str(a+b))
    break

