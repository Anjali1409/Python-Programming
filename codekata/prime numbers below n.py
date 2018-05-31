n=int(input())
for i in range(n):
    if(i>1):
        for x in range(2,i):
            if(i%x==0):
                break
        else:
            print('',i,end='')
