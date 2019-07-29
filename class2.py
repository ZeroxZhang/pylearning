# self的意思是，eat这个函数属于student
# 疑问：为什么name要放在self后面程序才能运行？
class Student:
    def eat(self, name, age):
        print(name + ' is able to eat and he is '+ str(age) +' years old')


Student().eat('zerox',28)

def print_nums(x):
  for i in range(x):
    print(i)
    return
print_nums(10)

#下面这个函数等同于0+0+1+2+3
def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))


