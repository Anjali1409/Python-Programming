n=int(input())
if(n>=1 and n<=10000):
    ni=(list(map(int,input().split())))
    li=[]
    for i in ni:
        if(i<n):
            li.append(i)
print(sorted(li))
