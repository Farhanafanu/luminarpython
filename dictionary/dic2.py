dict={'name':'arun','job':'engineer','location':'kochi'}
u={'location':'kochi','age':'25'}
for i in dict:
   if i in u:
        print(i)
def key(x):
    if x in dict:
        print("present")
    else:
        print("not present")
x=input("enter key")
key(x)
