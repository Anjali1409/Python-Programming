import re
s=input()
if(len(s)<=1000):
    spch=len(s)-len(re.findall('[\w]',s))
    print(spch)
