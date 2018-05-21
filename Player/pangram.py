a=input()
if(len(set('abcdefghijklmnopqrstuvwxyz') - set(a.lower())) ==0):
    print('yes')
else:
    print('no')
