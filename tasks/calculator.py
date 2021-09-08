def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
print("select operation")
print("1.add")
print("2 sub")
print("3.multply")
print("4.div")
while True:
    choice=input("enter the choice")
    num1 = int(input("enter the number"))
    num2 = int(input("enter the number"))
    if choice=='1':
        print((add(num1,num2)))
    elif choice=='2':
        print((sub(num1,num2)))
    elif choice=='3':
        print((mul(num1,num2)))
    elif choice=='4':
        print((div(num1,num2)))
        break
    else:
        print("invalid")



