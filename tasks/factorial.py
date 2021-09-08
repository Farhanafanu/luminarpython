num=int(input("enter the number"))
if num>=1:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    print(fact)
elif fact==0:
    print("fact of zero is 1")
else:
    print("fact does not exist")