a=int(input())
if(a>=1 and a<=100000):
    for i in range(a):
        if(a==i**2):
            print('yes')
            break
else:
    print('no')
