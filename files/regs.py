import re
f2=open("valid",'w')
x="([l][u][m]\d{2}[p][y][\d]{3}$)"
f=open("reg",'r')
for num in f:
    print(num)
    number=num.rstrip("\n")
    print(number)
    matcher=re.fullmatch(x,number)
    if matcher!=None:
        f2.write(number)
        f2.write("\n")
