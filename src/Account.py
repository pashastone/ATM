#Class to store account data
#Actions include Withdrawal, Deposit, and Set Balance
class Account:

    def __init__(self, balance: int, account_name: str):
        self.Balance = balance
        self.Account_Name = account_name

    def Withdraw(self, balance_change):
        if (self.Balance - balance_change) < 0:
            return -1
        else:
            self.Balance -= balance_change
            return self.Balance

    def Deposit(self, balance_change):
        self.Balance += balance_change
        return self.Balance

    def Set_Balance(self, new_balance):
        self.Balance = new_balance