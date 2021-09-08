set1={2,3,4,5,6,7,8,9,10,11,12,13}
prime=set()
notprime=set()
for i in set1:
    if i>1:
        for j in range(2,i):
             if i%j==0:
                notprime.add(i)
                break
             else:
                prime.add(i)
print(prime)
print(notprime)

