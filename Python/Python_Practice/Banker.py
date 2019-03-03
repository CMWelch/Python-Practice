class Banker:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Overdraft! Cannot withdraw this much")
        else:
            self.balance = self.balance - amount

    def __str__(self):
        return f"Account Owner: {self.owner}\nAccount Balance: {self.balance}\n"


acct = Banker("Connor", 2119.89)
print(acct)

acct.deposit(300)
print(acct)

acct.withdraw(100000)
print(acct)
