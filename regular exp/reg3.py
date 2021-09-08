# import re
# x='[abc]'
# matcher=re.finditer(x,'c@5kzabc')
# for match in matcher:
#     #print(match.start())
#     print(match.group())


# import re
# x='[A-Za-z]'
# matcher=re.finditer(x,"abt9c@KAZ")
# for match in matcher:
#     #print(match.start())
#     print(match.group())
# import re
# x='[0-9]'
# matcher=re.finditer(x,"abt9c@kAZ")
# for match in matcher:
#     print(match.start())
#     print(match.group())
# import re
# x='[A-Z]{1}[a-z]'
# count=0
# n=input("enter string")
# matcher=re.finditer(x,n)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     count+=1
import re
x='^a\db$'
n=input("enter string")
matcher=re.findite(x,n)
for match in matcher:
    print(match.start())
    print(match.group())