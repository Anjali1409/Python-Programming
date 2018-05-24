a,b=input().split()
a=int(a)
b=int(b)
if(a<=100000 and b<=100000):
    t=a
    a=b
    b=t
print(a,b)
