import random
n=input()
if(len(n)>=1 and len(n)<=100000):
    print(''.join(random.sample(n,len(n))))
