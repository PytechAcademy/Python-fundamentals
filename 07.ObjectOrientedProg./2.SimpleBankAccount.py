class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient balance."

# Creating an object of the Account class
account1 = Account("John", "1234567890", 1000)

print(account1.get_balance())  # Output: 1000
print(account1.withdraw_money(500))  # Output: 500
print(account1.get_balance())  # Output: 500
print(account1.withdraw_money(1000))  # Output: "Insufficient balance."