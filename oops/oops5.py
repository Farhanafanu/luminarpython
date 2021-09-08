class Bank:
    def accreate(self,acno,name,bname):
        self.bname=bname
        self.acno=acno
        self.name=name
        self.minimumbal=500
        self.balace=self.minimumbal
    def deposit(self,amt):
        self.amt=amt
        self.balace+=self.amt
        print("your",self.bname,"account has been credited with",self.amt)
        print("your current balance",self.balace)
    def withraw(self,amnt):
        self.amnt=amnt
        if self.amnt>self.balace:
            print("insuffishiont")
        else:
            print("account debited with",self.amnt)
            self.balace-=self.amnt
            print("available balance",self.balace)
obj=Bank()
#num=int(input("enter acount no"))
obj.accreate(123,'abc','sbi')
obj.deposit(2500)
obj.withraw(1500)