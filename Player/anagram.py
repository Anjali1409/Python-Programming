a='dhoni'
b=input()
if(len(b)<=100000):
    a1=list(a)
    a1.sort()
    a2=list(b)
    a2.sort()
    if(a1==a2):
        print('yes')
    else:
        print('no')
