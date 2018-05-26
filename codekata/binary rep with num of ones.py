import numpy as np
n,m=input().split()
n=int(n)
m=int(m)
b=np.bitwise_or(n,m)
br=("{0:b}".format(b))
print(br.count('1'))
    
    
        
