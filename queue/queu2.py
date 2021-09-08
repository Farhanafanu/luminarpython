que=[]
size=int(input("enter size"))
frond=0
rear=0
n=0
def insert():
    global frond,rear,size,que
    if rear>size:
        print("que is full")
    else:
        p=int(input("enter elemnt"))
        que.insert(rear,p)
        rear+=1
        for i in range(frond,rear):
            print(que[i])
def delete():
    global frond,rear,size,que
    if rear==frond:
        print("que is empty")
    else:
        frond+=1
        for i in range(frond,rear):
            print(que[i])
while n!=1:
    print("enter option")
    opt=int(input(" option1.insert2.delete"))
    if opt==1:
        insert()
    else:
        delete()