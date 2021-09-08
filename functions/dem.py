def add():
   num1=int(input("enter the number"))
   num2=int(input("enter the number"))
   res=num1+num2
   print("result is",res)
add()
#add()

#def oddcheck():
 #   num=int(input("enter the number"))
  #  if num%2==0:
     #   print("not odd")
 #   else:
   #     print("odd")
#oddcheck()
def factorial(fact):
    f=1
    if fact>0:
       for i in range (1 ,fact+1):
            f=f*i
       print("factorial is",f)
    elif fact==0:
       print("factorial of zero is 1")
    else:
       print("factorial does not exist")

factorial(7)
factorial(0)
factorial(-5)
