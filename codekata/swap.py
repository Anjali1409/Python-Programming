n,m=input().split()
n=int(n)
m=int(m)
if(n<=100000 and m<=100000):
    t=n
    n=m
    m=t
print(n,m)
