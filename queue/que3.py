que=[]
size=int(input("enter size"))
frond=0
rear=0
n=0
def insert():
    global size,frond,rear,que
    if rear>size:
        print("que is full")
    else:
        p=int(input("ener elemnt"))
        que.insert(rear,p)
        rear+=1
        for i in range(frond,rear):
            print(que[i])
def delete():
    global size,frond,rear,que
    if frond==rear:
        print("que is empty")
    else:
        frond+=1
        for i in range(frond,rear):
            print(que[i])
while n!=1:
    print("option to perormed")
    opt=int(input("enter option1.enque2.deque"))
    if opt==1:
        insert()
    else:
        delete()