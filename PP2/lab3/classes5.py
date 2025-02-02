class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
            self.balance += amount
            print(f"New balance: ${self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal exceeds balance")
        else:
            self.balance -= amount
            print(f"New balance: ${self.balance}")

account = Account("John Doe", 100)
print(f"Balance: ${account.balance}")
account.deposit(50)
account.withdraw(30)
account.withdraw(150)
print(f"Balance: ${account.balance}")