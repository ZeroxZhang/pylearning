#list comprehension,列表解析式
#需求：从0-10，每个乘以2，然后放在新的列表里

#常规写法
newlist = []
for i in range(11):
    newlist.append(i*2)

print(newlist)

#列表解析式写法
print([i*2 for i in range(11)])

#需求二：从名字列表中，查找姓张的,并放在新的list中

namelist = ["张一","张二","王3","王4"]
'''复杂写法'''
emptylist =[]
for name in namelist:
    if name.startswith("张"):
        emptylist.append(name)
print(emptylist)

'''列表解析式写法'''
print([name for name in namelist if name.startswith("张")])
