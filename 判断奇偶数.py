#以下为判断奇偶数
import random
r = random.randrange(1, 1000)
# 请暂时忽略以上两句的原理，只需要了解其结果：
# 引入随机数，而后，每次执行的时候，r 的值不同

if r % 2 == 0:
    print(r, 'is even.')
else:
    print(r, 'is odd.')

#以下为找到质数
for n in range(2, 100): #range(2,100)表示含左侧 2，不含右侧 100，是不是第三次看到这个说法了？
    if n == 2:
        print(n)
        continue
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:
        print(n)