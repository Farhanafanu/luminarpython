fixedamount=1000
withdraw=int(input("enter rupees"))
if withdraw<=fixedamount:
    balance=fixedamount-withdraw
    print(balance)
else:
    print("insuffisiont")