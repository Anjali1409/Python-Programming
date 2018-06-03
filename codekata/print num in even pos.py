n=(list(map(int,input().split())))
li=[]
count=0
for i in n:
    if(count%2==1):
        li.append(i)
    count+=1
print(li)
