import numpy as np
n=int(input())
ni=(list(map(int,input().split())))
for i in range(0,n):
    for j in range(i+1,n):
        p=np.bitwise_and(ni[i],ni[j])
print(p)
