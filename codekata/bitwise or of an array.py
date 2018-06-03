import numpy as np
n=int(input())
if(n<=100000):
    ni=(list(map(int,input().split())))
    arr=np.array(ni)
    print(np.bitwise_or.reduce(arr))
