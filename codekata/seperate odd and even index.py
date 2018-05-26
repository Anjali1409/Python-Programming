n=input()
res=""
re=""
for i in range(len(n)):
    if(i%2==0):
        res=res+n[i]
    else:
        re=re+n[i]
print(res,re)
        
