# quantifies
# x='a+'a including group
# x='a*'count including zeronumber of a
# x='a?'count a as each including zero no of a
# x='a{2}'2 no of position
# x='a{2,3}'minimum 2 a and maximum 3 a
# x='^a' check starting with a
#x='a$' check ending with a
# import re
# x='a+'
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
# import re
# x='a*'
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
import re
x='a?'
r='aaa abc aaaa cga'
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())