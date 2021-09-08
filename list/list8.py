list=[1,2,2,3,4,3,4,5,6]
dup=[]
for i in list:
    if i not in dup:
        dup.append(i)
    else:
       print(i)


