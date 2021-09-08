 #     print("invalid")
# import re
# n=input("enter kg")
# x='[0-9]{2}[a-z]{2}'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")


# import re
# n=input("enter number")
# x='[+][9][1]\d{10}$'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")
# import re
# n=input("enter string")
# x='^[A-Z]\w{5,10}[A-Z]$'
# match=re.fullmatch(x,n)
# if match is not  None:
#     print("valid ")
# else:
#     print("invalid")
import re
n=input("enter string")
x='^a{1}[0-9][b]$'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")