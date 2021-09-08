#def prime(num1,num2):
num1=int(input("enter the number"))
num2=int(input("enter max range"))
sum=0
for i in range(num1,num2+1):
    for j in range(2,i):
        if i%j==0:
            break
        else:
         print(i,"prime")
         sum=sum+i
print("sum of prime",sum)



