n,m=input().split()
n=int(n)
m=int(m)
count=0
n=(list(map(int,input().split())))
for num in n:
    if(num==m):
        count+=1
if(count==0):
    print('no')
else:
    print('yes',count)

