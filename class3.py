# 把变量预定义在class内function外，这个时候在function里引用的话，需要在变量前+self.

class Student:

    name = "zerox"
    age = 28

    def eat(self):
        print(self.name + ' is able to eat and he is '+ str(self.age) +' years old')


Student().eat()



