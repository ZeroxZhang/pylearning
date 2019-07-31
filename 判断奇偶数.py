#函数def=define
import random
r = random.randrange(1, 1000)
# 请暂时忽略以上两句的原理，只需要了解其结果：
# 引入随机数，而后，每次执行的时候，r 的值不同

if r % 2 == 0:
    print(r, 'is even.')
else:
    print(r, 'is odd.')