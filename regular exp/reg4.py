import re
x='[A-Za-z0-9]'
matcher=re.finditer(x,"abt9c@kAZ")
for match in matcher:
    #print(match.start())
    print(match.group())
import re
x='\w'
matcher=re.finditer(x,"abtAc@KAZ")
for match in matcher:
    #print(match.start())
    print(match.group())
import re
x='\W'
matcher=re.finditer(x,'abtc@5kz')
for match in matcher:
    print(match.start())
    print(match.group())
import re
x='\d'
matcher=re.finditer(x,'abtc@5kz')
for match in matcher:
    print(match.start())
    print(match.group())