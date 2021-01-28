from src.Bank import Bank

#Class to define an ATM object. Is both interactable and an API
#ATM can have multiple banks (And no fees!)
class ATM:
    def __init__(self):
        #set initial states
        self.State = "Start"
        #Dictionary of loaded banks
        self.Banks = {}
        # Save States of Selections
        self.Selected_Bank = None
        self.Selected_Client = None
        self.Selected_Account = None
        #Update options
        self.Update_Options()

    #Updates options on screen based on state
    def Update_Options(self):
        if self.State == "Start":
            self.Options = ["Start"]
        elif self.State == "Select Bank":
            self.Options = self.Get_All_Banks()
        elif self.State == "Insert Card":
            self.Options = ["Insert Bank Card"]
        elif self.State == "Enter Pin":
            self.Options = ["Enter Pin Number"]
        elif self.State == "Select Account":
            self.Options = self.Selected_Client.Get_All_Accounts()
        elif self.State == "Choose Action":
            self.Options = ["Withdraw", "Deposit", "Check Balance"]
        elif self.State == "Withdraw":
            self.Options = ["Enter Amount"]
        elif self.State == "Deposit":
            self.Options = ["Please Insert Cash"]
        elif self.State == "Check Balance":
            self.Options = [("Current Balance: $" + str(self.Selected_Account.Balance))]
        else:
            self.Options = ["404 Error: State Undefined"]

    #Prints out options as expected on ATM screen
    def Display_Options(self):
        print("Please Select From The Following:\n")
        index = 1
        for Option in self.Options:
            print("Option " + str(index) + ": " + Option)
            index+=1
        #Back option avaliable on all but start screen
        if self.State != "Start":
            print("Back")

    #Go back to previous screen/state
    def Back(self):
        if self.State == "Select Bank":
            self.State = "Start"
        elif self.State == "Insert Card":
            self.State = "Select Bank"
        elif self.State == "Select Account":
            self.State = "Insert Card"
        elif self.State == "Enter Pin":
            self.State = "Insert Card"
        elif self.State == "Select Account":
            self.State = "Enter Pin"
        elif self.State == "Choose Action":
            self.State = "Select Account"
        elif self.State in ["Deposit", "Withdraw", "Check Balance"]:
            self.State = "Choose Action"
        self.Update_Options()

    #Numbered enter, Only applies to Pin and Withdrawal
    def Number_Entered(self, entry: str):
        if self.State == "Withdraw":
            New_Balance = self.Selected_Account.Withdraw(int(entry))
            #Check if insufficent funds
            if New_Balance == -1:
                self.Options = ["Insufficent Funds! Re-Enter Withdrawal Amount"]
            else:
                self.Options = [str("New Balance is $" + str(New_Balance))]
        elif self.State == "Enter Pin":
            #Check if pin is correct
            if self.Selected_Bank.Check_Pin(self.Selected_Account, entry):
                self.State = "Select Account"
                self.Update_Options()
            else:
                self.Options = ["Incorrect Pin! Try Again"]

    #Take card number string as input and looks up account with bank
    def Insert_Card(self, card_number: str):
        if self.State == "Insert Card":
            self.Selected_Client = self.Selected_Bank.Get_Client(card_number)
            #check if this account exists with this bank
            if (self.Selected_Client):
                self.State = "Select Account"
                self.Update_Options()
            else:
                self.Options = ["Account Doesn't Exist With This Bank! Insert New Card"]

    #Update account balance based on deposited cash
    def Insert_Cash(self, Amount: int):
        if self.State == "Deposit":
            New_Balance = self.Selected_Account.Deposit(Amount)
            self.Options = [str("New Balance is $" + str(New_Balance))]

    #Make selection based on screen options
    #You can display the options to look at what number corresponds to what Option
    #Keep in mind the screen is 1 based, while the array of options is 0 based
    def Select(self, Selection: int):
        if Selection <= len(self.Options):
            Selected_Option = self.Options[(Selection - 1)]
            if self.State == "Select Bank":
                self.Selected_Bank = self.Banks.get(Selected_Option)
                self.State="Insert Card"
            elif self.State == "Select Account":
                self.Selected_Account = self.Selected_Client.Get_Account(Selected_Option)
                self.State="Choose Action"
            elif self.State == "Choose Action":
                self.State = Selected_Option
            elif self.State == "Start":
                self.State = "Select Bank"
            self.Update_Options()

    #Bank Add/Delete/Get API
    def Add_Bank(self, new_bank: Bank):
        self.Banks[new_bank.Name] = new_bank

    def Delete_Bank(self,bank_name: str):
        del self.Banks[bank_name]

    def Get_Bank(self,bank_name: str):
        return self.Banks.get(bank_name)

    #Lists keys to all banks in dictionary (Key is the bank name string)
    def Get_All_Banks(self):
        return list(self.Banks.keys())

