class BankAccount:

    all_accounts = []

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if BankAccount.check_balance(self.balance,amount): 
            self.balance -= amount
        else:
            print("Insufficient Funds.")
        return self

    @staticmethod
    def check_balance(balance,amount):
        if balance < amount:
            return False
        else:
            return True

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance*self.int_rate
        else:
            return False 
        return self
    
    @classmethod
    def all_acc_info(cls):
        sum = 0
        for account in cls.all_accounts:
            sum+= account.balance
        return sum

taher_account = BankAccount()
taher_account.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()

troy_account = BankAccount()
troy_account.deposit(200).deposit(200).withdraw(100).withdraw(100).withdraw(100).withdraw(200).yield_interest().display_account_info()

print(BankAccount.all_acc_info())

