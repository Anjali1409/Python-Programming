n=input().split()
n=[int(i) for i in n]
while(len(n)!=1):
    if(n[0]>n[1]):
        n.remove(n[1])
    else:
        n.remove(n[0])
print(n[0])
