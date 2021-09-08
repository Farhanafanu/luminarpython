a={1,2,3,4,5,6,7,8,9,10}
b=set()
for i in a:
    s=i*i
    if i not in b:
        b.add(s)
print(b)
