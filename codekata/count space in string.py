s=input()
if(len(s)<=1000):
    space=sum(c.isspace() for c in s)
    print(space)
