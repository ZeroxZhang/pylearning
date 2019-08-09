# Class: init method. init=initialize,初始化
#
# class Student:
#     name = "zerox"
#     age = 18
#     def walk(self):
#         print(self.name,"can work")
#         print(self.name,"is",self.age)
#
# S1 = Student()
# S1.walk()
# #上面的代码会导致打印出来的name和age是固定的。
# #因此引入init方法如下

class Student2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def walk(self):
        print(self.name,"can work")
        print(self.name,"is",self.age)

s2 = Student2(name="zerox",age="28") #要把初始化变量放在赋予类的括号里
s3 = Student2("robbie",27) #也可以直接把相应的变量写进去，不用写name=
s2.walk()
s3.walk()



