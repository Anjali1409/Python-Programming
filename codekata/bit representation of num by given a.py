a=int(input())
if(a>=1 and a<=1000):
    n=2**a
    for i in range(0,n):
        print(format(i, '#0{}b'.format(a + 2)).replace('0b', ''))
