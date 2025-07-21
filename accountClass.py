class Account:
    def __init__(self, account_number, pin, balance):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"You added {amount} to your account. Now the balance is {self.balance}")
        else:
            print("Incorrect input: The amount should be greater than 0")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            print(f"You withdrew {amount} from your account. Now the balance is {self.balance}")
        else:
            print("Incorrect withdraw input")
