import numpy as np
n,m=input().split()
n=int(n)
m=int(m)
if(1<=n and m<=1000):
    print(np.left_shift(n,m))
