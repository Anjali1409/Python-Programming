import numpy as np
n=int(input())
ni=(list(map(int,input().split())))
for num in ni:
    p=np.bitwise_and(num,num+1)
print(p)
