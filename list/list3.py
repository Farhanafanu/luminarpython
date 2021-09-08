#list1=[1,2,[4,5,6,[7,8,9]]]
#print(list1)
#list is mutable

#del list1
max=int(input("enter max range"))
sum=0
for num in range(2,max+1):
    for i in range(2,num):
        if num%i==0:
            break

