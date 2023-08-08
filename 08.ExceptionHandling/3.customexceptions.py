class WithdrawalError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Error: Insufficient balance ({balance}) for withdrawal of {amount}")

def make_withdrawal(balance, amount):
    if balance < amount:
        raise WithdrawalError(balance, amount)
    return balance - amount

try:
    account_balance = 100
    withdrawal_amount = 150
    new_balance = make_withdrawal(account_balance, withdrawal_amount)
except WithdrawalError as e:
    print(e)

# Output: Error: Insufficient balance (100) for withdrawal of 150