import re
n=input("enter reg number")
x='[k][l][0-9]{2}[a-z]{2}\d{4}$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
import re
n=input("enter string")
x='[a-z A-Z]+\d{1}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("not valid")
import re
n=input("enter gmail")
x='[a-zA-Z0-9]+[@][a-z]+[.][a-z]{2,3}$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
import re
n=input("enter string")
x='^a[a-zA-Z0-9\W]*b$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
import re
n=input("enter string")
x='[a-zA-Z\W]{8,15}\D'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
import re
n=input("enter string")
x='(^[A-Z]{1}[a-z\d\w]*)'
match=re.fullmatch(x,n)
if match is not None:
 print("invalid")