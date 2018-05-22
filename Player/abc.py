d=int(input())
if(d>=1 and d<=100000):
        print(sum(int(x)**2 for x in str(d)))
