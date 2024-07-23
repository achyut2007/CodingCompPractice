class Account:
    def __init__(self , accNum, accHoldName, balance):
        self.num = accNum
        self.holdName = accHoldName
        self.bal = balance
    def __str__(self):
        return f"Account No.: {self.num}\nAccount Holder Name: {self.holdName}\nBalance: Rs.{self.bal}"
    def deposit(self, amt):
        print(f"Current Balance:{self.bal}")
        self.bal+=amt
        print(f"New Balance:{self.bal}")
    def withdraw(self, amt):
        if self.bal >= amt:
            print(f"Current Balance:{self.bal}")
            self.bal-=amt
            print(f"New Balance:{self.bal}")
        else:
            print("You don't have enough balance to withdraw this amount.")


PKP = Account(123432, "PKP", 10.00)
print(PKP)
# PKP.deposit(20.0)
PKP.withdraw(100.0)