class InsufficientBalanceException(Exception):
    pass

class SavingsAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceException("Withdrawal amount exceeds available balance.")
        self.balance -= amount
        print(f"Withdrew {amount}. Remaining balance: {self.balance}")

account = SavingsAccount(1500)

try:
    account.withdraw(2000)
except InsufficientBalanceException as e:
    print(e)
