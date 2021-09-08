import  re
count=0
matcher=re.finditer('ab','abbabbab')
print(matcher)
for match in matcher:
    print("match available at",match.start())
    print("group=",match.group())
    count+=1
print("count=",count)
import re
#count=0
matcher=re.finditer('ac','accbdcacacbsac')
print(matcher)
for match in matcher:
    print("match availe at",match.start())
    print("group",match.group())
    #count+=1
print("count",count)