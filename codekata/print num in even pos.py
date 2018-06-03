n=(list(map(int,input().split())))
li=[]
count=0
for i in n:
    if(count%2==1):
        li.append(i)
    count+=1
print(li) 
              (or)
n=(list(map(int,input().split())))
li=n[1::2]
print(li) (or)
