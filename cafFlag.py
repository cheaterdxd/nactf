import re
p = open('flag.txt','r')
for i in p:
    if re("nactf{[a-zA-Z0-9_]{48}[aoeui]}",i):
        print(i)
