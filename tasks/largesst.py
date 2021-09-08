no1=int(input("enter the first element"))
no2=int(input("enter the second element"))
no3=int(input("enter the third element"))
if (no1>no2)&(no1>no3):
    print("no1 is greater")
elif (no2>no1)&(no2>no3):
    print("no2 is greater")
elif no1==no2==no3:
    print("equal")
else:
    print("n3 is greater")