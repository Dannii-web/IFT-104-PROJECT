from account import Account

class CurrentAccount(Account):
    def __init__(self, balance):
        Account.__init__(self, balance)

    def withdraw(self, amount):
        super().withdraw(amount)

    def deposit(Self, amount):
        super().deposit(amount)

