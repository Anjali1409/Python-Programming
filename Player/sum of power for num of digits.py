x=int(input())
n=len(str(x))
if(x>=1 and x<=100000000000):
        print(sum(int(i)**n for i in str(x)))
