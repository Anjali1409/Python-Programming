import re
import sys
s=sys.stdin.read()
if(len(s)<=1000):
    sp=len(re.split('\n',s))
    print(sp)
