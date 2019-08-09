#可以简单的理解为，mocode是一堆.py文件的组合，ipt是其中一个.py文件
from mycode import ipt

ipt.eat()

#以下是requests库的引入
import requests
baidu = requests.get("https://www.baidu.com/")
print(baidu)#这个是返回请求的状态
print(baidu.content)#这个是返回内容