import fractions
n,q=input().split()
n=int(n)
q=int(q)
if(n>=1 and n<=100000):
    n=(list(map(int,input().split())))
    for i in range(0,q):
        j,k=input().split()
        j=int(j)
        k=int(k)
        x=j-1
        y=k-1
        sum=0
        for z in range(x,y+1):
            sum+=n[z]
        print(sum)
