n=int(input())
ni=(list(map(int,input().split())))
li=[]
for i in ni:
    if(i<n):
        li.append(i)
print(sorted(li))
