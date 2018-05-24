import re
s=input()
spch=len(s)-len(re.findall('[\w]',s))
print(spch)
