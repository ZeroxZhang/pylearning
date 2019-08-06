class Father:
    def eat(self):
        surname = "zhang"
        print("Father can eat")

class Mother:
    def cook(self):
        print("mom can cook food")
#son继承father的属性，在类括号中写入要继承属性的类名
class Son(Father,Mother):#继承的时候用逗号隔开多个类
    def eat(self):
        print("这句话重载了father eat的方法")
    def cook(self):
        print("mom does not like cook")
#如果继承类之后，这个类有相同的方法，那么则会重载父类的方法
littlezerox = Son()
littlezerox.eat()
littlezerox.cook()


