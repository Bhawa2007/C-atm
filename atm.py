
class Atm(object):
    def __init__(self,Name,Cashwithdrawl,BalanceEnquiry,deposit):
        self.name1=Name
        self.cashwithdrawl1=Cashwithdrawl
        self.BalanceEnquiry1=BalanceEnquiry
        self.deposit1=deposit
      
    def cashwithdrawl2(self):   
        print("$100 withdrawed")

    def balanceenquiry2(self):
        print("Your balance is $250")

Customer=Atm("Brock",54,"$100",'$300')
Customer.cashwithdrawl2()
print(Customer.name1)