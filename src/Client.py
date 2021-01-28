from src.Account import Account

#Class of a Client to a bank
#Client can have multiple accounts
class Client:
    def __init__(self, pin: str, card_number: str, name: str):
        #Save Client information
        self.Pin = pin
        self.Card_number = card_number
        self.Name = name
        #Make Dictionary of accounts
        self.Accounts = {}

    #Add, Delete, Get, and List API for accounts belonging to client
    def Add_Account(self, account_name: str):
        #Test is account name already exists
        if self.Accounts.get(account_name):
            return False
        else:
            #All new accounts start with balance of 0
            New_Account = Account(0, account_name)
            self.Accounts[account_name] = New_Account
            return True

    def Delete_Account(self, account_name: str):
        del self.Accounts[account_name]

    def Get_Account(self, account_name: str):
        return self.Accounts.get(account_name)

    def Get_All_Accounts(self):
        return list(self.Accounts.keys())