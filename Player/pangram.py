a=input()
if(len(a)<=10000):
    if(len(set('abcdefghijklmnopqrstuvwxyz') - set(a.lower())) ==0):
        print('yes')
    else:
        print('no')
