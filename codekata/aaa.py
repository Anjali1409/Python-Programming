import numpy as np
n=int(input())
if(n<=100000):
    li=(list(map(int,input().split())))
    ar=np.array(li)
    print(np.bitwise_or.reduce(ar))
