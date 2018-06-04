n=int(input())
if(n>=1 and n<=10000000000):
    ni=list(map(int,str(n)))
    sum=0
    for num in ni:
        if(num%2!=0):
            sum=sum+num
    if(sum%2!=0):
        print('O')
    else:
        print('E')
