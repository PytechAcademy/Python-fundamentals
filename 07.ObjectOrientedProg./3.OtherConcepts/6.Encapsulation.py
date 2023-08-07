class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance  # Private attribute using name mangling

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


account = BankAccount("123456789", 1000)
print(account.get_balance())  # Output: 1000

account.deposit(500)
print(account.get_balance())  # Output: 1500

account.withdraw(800)
print(account.get_balance())  # Output: 700