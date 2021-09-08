num1=int(input("enter one number"))
num2=int(input("enter 2d number"))
try:
     print(num1/num2)
except Exception as a:
  print(a.args)
a=int(input("enter"))
b=int(input("enter"))
if b>a:
    raise Exception("no2 is greater")
else:
    print(a/b)
age=int(input("enter age"))
if age>=18:
   print("eligible for vaccination")
else:
    raise Exception("not eligible for vaccination")
age=int(input("enter age"))
if age>=10:
    print("eligible for tour")
else:
    raise Exception("not eligible for tour")