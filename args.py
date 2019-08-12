# def sum(c,d):
#     print(c+d)
#
# sum(2,3)

#如果遇到需要很多变量怎么办？

def sum2(*args):
    print(sum(args))

sum2(1,2,3,3,5,6)

def love(*args):
    for name in args:
        print("I love ",name)

love("xiaowang","zerox","robbie")