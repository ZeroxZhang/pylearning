# if_name_main_被调用 这个文件的代码为：
#def m1():
#     print("this is m1 to be imported")
# m1()

import if_name_main_被调用
def m2():
    print("this is m1 module")
m2()
if_name_main_被调用.m1()#被import的py中加入了ifnamemain,所以夸文件调用必须使用这行代码才能用
#这个时候打印出来的结果为：m1 和 m2的内容
#this is m1 to be imported
# this is m1 module