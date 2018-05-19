a=int(input())
sum=0
t=a
while(t>0):
    digit=t%10
    sum+=digit**3
    t//=10
if(a==sum):
    print("yes")
else:
    print("no")
                
