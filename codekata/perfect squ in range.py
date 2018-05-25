l,r=input().split()
l=int(l)
r=int(r)
count=0
for i in range(l,r+1):
    if(int(i**0.5)**2==int(i)):
        count=count+1
print(count)
