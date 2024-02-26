class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: {}. New balance: {}".format(amount, self.balance))
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrew: {}. New balance: {}".format(amount, self.balance))
        else:
            print("Withdrawal declined")

account = BankAccount("Alim", 100.00)

account.deposit(50.00)
account.withdraw(25.00)
account.deposit(100.00)
account.withdraw(389.00)

print("Account owner: {}".format(account.owner))
print("Account balance: {}".format(account.balance))
    