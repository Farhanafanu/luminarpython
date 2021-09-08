a=input("enter the string")
#
#a=input("enter string")
s="@!#$%^&*()~1234567890{}.,;"
b=""
for i in a:
    if i not in s:
       b+=i
print(b)