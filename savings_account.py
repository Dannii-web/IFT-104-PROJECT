from account import Account

class savingsAccount(Account):
    def __init__(self,balance):
        Account.__init__(self,balance)

    def withdraw(self, amount):
        if amount <= 10000:
            super().withdraw(amount)
        else:
            print("withrawal limit exceeded")

    def deposit(self,amount):
        super().deposit(amount)

