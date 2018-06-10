import numpy as np
import random
n,m=input().split()
n=int(n)
m=int(m)

a=np.zeros(n)
b=np.ones(m)
c=(list(map(int,a)))
d=(list(map(int,b)))
x=c+d
random.shuffle(x)
print(x)

