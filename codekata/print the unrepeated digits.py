n=(list(map(int,input().split())))
ni=[]
for i in n:
    p=n.count(i)
    if(p==1):
        ni.append(i)
print(ni)
