n=int(input())
ni=input().split()[:n]
a=ni[0:len(ni)//2]
b=ni[len(ni)//2:]
print(sorted(a)+sorted(b,reverse=True))
