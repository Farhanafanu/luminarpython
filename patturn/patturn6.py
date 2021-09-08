def parellal(n):
    k = n
    print(k)
    for i in range(n):
        for r in range(k):
            print(end=" ")
            k=k+1
            for j in range(n):
                print("*",end="")
            print("\r")
parellal(4)