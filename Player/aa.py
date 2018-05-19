a,b=input().split()
a=int(a)
b=int(b)
if(a<=100000):
    if(b<=10000):
        for i in range(a+1,b):
            if(i%2!=0):
                print(i)
