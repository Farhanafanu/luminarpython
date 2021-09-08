# s={1,2,3,4,5,6,7,8,9,10}
# odd=set()
# even=set()
# for i in s:
#     if i%2==0:
#      even.add(i)
#     else:
#         odd.add(i)
# print(even,odd)
s={1,2,3,4,5,6,7,8,9,10}
odd=set()
even=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(odd,even)