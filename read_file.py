#读写文件
file = open("data.txt")#同一个文件夹，直接写文件名即可
t = file.read()
print(t)
file.close()#这种写法一定要close打开的文件，否则会一直占用内存

#等效代码,且不用close打开的文件
with open("D:\zerox.txt") as file2:
    print(file2.read())

#下面是写入内容,w参数会覆盖原本内容
with open("D:\zerox.txt","w") as file3:
    file3.write(",he is good")

#下面是写入内容,a参数会在原有内容基础上增加内容,\n用来换行
with open("D:\zerox.txt","a") as file4:
    file4.write("\n,he is good\n")