# mydic={"iphone":100,"huawei":1200}
# # print(mydic)
# ip=(mydic["iphone"])
# print("iphone's price:"+str(ip))
# mydic["iphone"]=5
# print(mydic)
# mydic.clear()
# print(mydic)

age= int(input("please input your age: "))
if age<21:
    print("you can not smoke")
elif age==21:
    print("you are legal")
else:
    print("you can smoke")