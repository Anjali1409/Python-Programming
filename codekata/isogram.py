n=input()
if(len(n)<=1000):
    if(len(n)==len(set(n))):
        print('yes')
    else:
        print('no')
        
