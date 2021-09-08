min=int(input("ente minimum range"))
max=int(input("enter max range"))
#print("prime numbers between",min,"and",max)
for i in range(min,max+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)




