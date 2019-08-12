#args and kwargs分别是什么，怎么样
#arges是元祖类型，kwargs是字典类型

def types(*args,**kwargs):
    print(type(args))
    print(type(kwargs))
types()

def namelist(**kwargs):
    for k,v in kwargs.items():
        print(k,":",v)

namelist(name="zerox",age="18")