class Atm(object):
    def __init__(self,CashWidrawl,bankEnquiry,CheckDiposit):
        self.Cashwidrawl=CashWidrawl
        self.bankEnquiry=bankEnquiry
        self. CheckDiposit=CheckDiposit

        
        

    def AtmCardNumber(self):
        input("What is your atm card number: ")

    def PinNumber(self):
        input("What is your pin number :")

    

    
Bank = Atm("$50","You used 150$ last week","$200 check",)
print(Bank.model)