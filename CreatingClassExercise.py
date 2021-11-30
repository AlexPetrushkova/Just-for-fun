class BankAccount():
    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.currency}{self.balance}" 

    def deposit(self, v):
        self.balance += v
        print("Deposit Accepted")

    def withdrawal(self, v):
        if v <= self.balance:
            self.balance -= v
            print("Funds withdrawn")
        else:
            print("Funds Unavailable!")

acct1 = BankAccount('Jose', 100, 'USD')
print(acct1)