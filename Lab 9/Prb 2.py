#Custom Error
class InsufficientFundsError(Exception):
    pass
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)
            print(f"Withdrew {amount}. New balance is {self.balance}.")

try:
    b = BankAccount(5000)
    b.withdraw(10000)

except InsufficientFundsError:
    print("Error: Insufficient funds")
