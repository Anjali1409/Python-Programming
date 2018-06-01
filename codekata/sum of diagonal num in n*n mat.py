import numpy as np
n=int(input())
if(n<=1000):
    mat1=[]
    for i in range(0,n):
        mat1.append(list(map(int,input().split())))
        b=np.trace(mat1)
    print(b)
    
