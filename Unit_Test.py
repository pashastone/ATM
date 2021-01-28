from src.Bank import Bank
from src.Client import Client
from src.Encrypt import Encrypt
from src.Account import Account
from src.ATM import ATM

#My Custom Test Bench Class
class Test_Bench:

    #Static variables to keep track of total test cases/cases passed
    def __init__(self, test_name: str):
        self.TotalTests = 0
        self.Passed = 0
        self.Test_Name = test_name

    #Will check if two inputted values (any data type) are equal
    #Can also check is not equal with optional input
    def Verify(self, test_value, expected_value, NotEqual=False):
        self.TotalTests += 1
        if (test_value == expected_value) ^ NotEqual:
            self.Passed += 1
        else:
            print("Expected: ", expected_value, " But got: ", test_value)

    def PrintResults(self):
        print(str(self.Test_Name + ": " + str(self.Passed) + "/" + str(self.TotalTests) + " Test Cases Passed"))


if __name__ == "__main__":
    ####### Test Encryption  Function ############################
    Encryption_Test = Test_Bench("Encryption Test")

    #Normal encryption key Test
    TestKey = 1234
    TestPin = "1111"
    ExpectedEncryption = "2345"
    TestEncryption = Encrypt(TestPin, TestKey)
    Encryption_Test.Verify(TestEncryption, ExpectedEncryption)

    #Test with rollover
    TestKey = 9234
    TestPin = "1111"
    ExpectedEncryption = "0345"
    TestEncryption = Encrypt(TestPin, TestKey)
    Encryption_Test.Verify(TestEncryption, ExpectedEncryption)

    #Test 0000 edge case
    TestKey = 8889
    TestPin = "1111"
    ExpectedEncryption = "0000"
    TestEncryption = Encrypt(TestPin, TestKey)
    Encryption_Test.Verify(TestEncryption, ExpectedEncryption)

    Encryption_Test.PrintResults()

    ####### Test Account Class ####################################
    Account_Test = Test_Bench("Account Test")
    Test_Account = Account(0, "Checking")
    #Test account is intialized properly
    Account_Test.Verify(Test_Account.Balance, 0)

    #Test set balance
    Test_Account.Set_Balance(100)
    Account_Test.Verify(Test_Account.Balance, 100)

    #Test Normal Withdrawal
    Test_Balance = Test_Account.Withdraw(50)
    Account_Test.Verify(Test_Balance, 50)

    #Test Withdrawal Edge Case
    Test_Balance = Test_Account.Withdraw(50)
    Account_Test.Verify(Test_Balance, 0)

    #Test overdraw
    Test_Balance = Test_Account.Withdraw(50)
    Account_Test.Verify(Test_Balance, -1)

    #Test deposit
    Test_Balance = Test_Account.Deposit(500)
    Account_Test.Verify(Test_Balance, 500)

    Account_Test.PrintResults()

    ####### Test Client Class ####################################
    Client_Test = Test_Bench("Client Test")
    Test_Client = Client("1111", "1111222233334444", "Pasha Stone")

    # Make sure client is intialized properly (name, $0 balance)
    Test_Client_Add = Test_Client.Add_Account("Checking")
    Client_Test.Verify(Test_Client_Add, True)
    Test_Client_Account = Test_Client.Get_Account("Checking")
    Client_Test.Verify(Test_Client_Account.Balance, 0)
    Client_Test.Verify(Test_Client_Account.Account_Name, "Checking")

    #Tests if account already exists and is handled properly
    Test_Client_Add = Test_Client.Add_Account("Checking")
    Client_Test.Verify(Test_Client_Add, False)

    #Test Deleting Account
    Test_Client.Delete_Account("Checking")
    Test_Client_Account = Test_Client.Get_Account("Checking")
    Client_Test.Verify(Test_Client_Account, None)

    ####### Test Bank Class ####################################
    Bank_Test = Test_Bench("Bank Test")
    Test_Bank = Bank("Test Bank", 4444)

    #Test adding client
    Test_Bank_Client_Number=Test_Bank.Add_Client("Pasha Stone","1111222233334444","1234")
    Bank_Test.Verify(Test_Bank_Client_Number,"1111222233334444")
    Bank_Test.Verify(Test_Bank.Get_Client("1111222233334444").Name, "Pasha Stone")

    #Test adding second client and testing card number interpherance
    #Should add second client under differant card number
    Test_Bank_Client_Number = Test_Bank.Add_Client("Pasha Stone 2", "1111222233334444", "1234")
    Bank_Test.Verify(Test_Bank_Client_Number, "1111222233334444",NotEqual=True)

    #Test pin number check
    Bank_Test.Verify(Test_Bank.Check_Pin(Test_Bank_Client_Number,"1234"),True)
    Bank_Test.Verify(Test_Bank.Check_Pin(Test_Bank_Client_Number, "1235"), False)

    #Test Deleting Client
    Test_Bank.Delete_Client("1111222233334444")
    Bank_Test.Verify(Test_Bank.Get_Client("1111222233334444"),None)

    Bank_Test.PrintResults()

    ####### Test Client Class ####################################

    ATM_Test=Test_Bench("ATM Test")

    #initialize ATM with 2 banks
    Test_ATM=ATM()
    Test_ATM_Bank_A= Bank("Bank A", 4444)
    Test_ATM_Bank_B = Bank("Bank B", 4444)
    Test_ATM.Add_Bank(Test_ATM_Bank_A)
    Test_ATM.Add_Bank(Test_ATM_Bank_B)
    #Test Adding Bank
    ATM_Test.Verify(Test_ATM.Get_Bank("Bank A"),Test_ATM_Bank_A)
    #Test Deleting Bank
    Test_ATM.Delete_Bank("Bank A")
    ATM_Test.Verify(Test_ATM.Get_Bank("Bank A"), None)

    #ATM Interface Test

    #Add a new bank
    #Let's makeup a name
    #Something that sounds like it has bad customer service
    #Like "Wells Fargo"
    ATM_Test_Bank = Bank("Wells Fargo", 1234)
    #This is my real credit card number and pin, please don't steal it :)
    ATM_Test_Bank_Client_Number = ATM_Test_Bank.Add_Client("Pasha Stone", "1111222233334444", "1234")
    ATM_Test_Bank_Client=ATM_Test_Bank.Get_Client(ATM_Test_Bank_Client_Number)
    #Add checking and savings account with $100, and $200 respectively (times are tough right now)
    ATM_Test_Bank_Client.Add_Account("Checking")
    ATM_Test_Bank_Client.Add_Account("Savings")
    ATM_Test_Bank_Client_Checking=ATM_Test_Bank_Client.Get_Account("Checking")
    ATM_Test_Bank_Client_Savings=ATM_Test_Bank_Client.Get_Account("Savings")
    ATM_Test_Bank_Client_Checking.Set_Balance(100)
    ATM_Test_Bank_Client_Savings.Set_Balance(200)
    Test_ATM.Add_Bank(ATM_Test_Bank)

    #Begin interaction test

    #Confirm start state
    ATM_Test.Verify(Test_ATM.Options, ["Start"])
    ATM_Test.Verify(Test_ATM.State, "Start")

    #Select 1 on the screen (only option)
    Test_ATM.Select(1)
    #Make sure we go to the select bank page,
    #And the correct banks are listed
    ATM_Test.Verify(Test_ATM.State, "Select Bank")
    ATM_Test.Verify(("Wells Fargo" in Test_ATM.Options), True)
    ATM_Test.Verify(("Bank B" in Test_ATM.Options), True)

    #Select our made up bank
    #Keep in mind for all selects there will be a +1
    #Due to the ATM button options not being 0 indexed
    Test_ATM.Select(Test_ATM.Options.index("Wells Fargo")+1)
    ATM_Test.Verify(Test_ATM.State, "Insert Card")

    #Insert card with a number that doesn't belong to this bank
    Test_ATM.Insert_Card("1111222211112222")
    #Verify card was rejected
    ATM_Test.Verify(Test_ATM.State, "Insert Card")
    ATM_Test.Verify(Test_ATM.Options, ["Account Doesn't Exist With This Bank! Insert New Card"])

    #Let's insert the correct card
    Test_ATM.Insert_Card(ATM_Test_Bank_Client_Number)
    ATM_Test.Verify(Test_ATM.State, "Select Account")

    #Verify correct accounts are displayed
    ATM_Test.Verify(("Checking" in Test_ATM.Options), True)
    ATM_Test.Verify(("Savings" in Test_ATM.Options), True)
    ATM_Test.Verify(len(Test_ATM.Options), 2)

    #Select checking account
    Test_ATM.Select(Test_ATM.Options.index("Checking") + 1)

    #make sure actions (Withdraw, Check Balance, and Deposit are diplayed
    ATM_Test.Verify(Test_ATM.State, "Choose Action")
    ATM_Test.Verify(("Withdraw" in Test_ATM.Options), True)
    ATM_Test.Verify(("Check Balance" in Test_ATM.Options), True)
    ATM_Test.Verify(("Deposit" in Test_ATM.Options), True)

    #Select check balance and confirm the page is as expected
    Test_ATM.Select(Test_ATM.Options.index("Check Balance") + 1)
    ATM_Test.Verify(Test_ATM.State, "Check Balance")
    ATM_Test.Verify(Test_ATM.Options,["Current Balance: $100"])

    #Go back, confirmed the back worked, and choose withdraw now
    Test_ATM.Back()
    ATM_Test.Verify(Test_ATM.State, "Choose Action")
    Test_ATM.Select(Test_ATM.Options.index("Withdraw") + 1)
    ATM_Test.Verify(Test_ATM.State, "Withdraw")

    #Let perform a very discouraging act of overdrawing your bank account
    #and make sure  everything is played properly
    Test_ATM.Number_Entered("200")
    ATM_Test.Verify(Test_ATM.Options, ["Insufficent Funds! Re-Enter Withdrawal Amount"])

    #Let's just empty the balance
    #Checking accounts have low interest anyways
    Test_ATM.Number_Entered("100")
    #Confirm correct new balance
    ATM_Test.Verify(Test_ATM.Options, ["New Balance is $0"])

    #Go back and select Savings Account
    Test_ATM.Back()
    Test_ATM.Back()
    ATM_Test.Verify(Test_ATM.State, "Select Account")
    Test_ATM.Select(Test_ATM.Options.index("Savings") + 1)
    Test_ATM.Select(Test_ATM.Options.index("Deposit") + 1)
    #Let's put the cash we just withdrew in savings
    Test_ATM.Insert_Cash(100)
    #Confirm new balance is as expected
    ATM_Test.Verify(Test_ATM.Options, ["New Balance is $300"])

    #Go all the way back to the start screen
    #Test if state is correct at each "Back" action
    Test_ATM.Back()
    ATM_Test.Verify(Test_ATM.State, "Choose Action")
    Test_ATM.Back()
    ATM_Test.Verify(Test_ATM.State, "Select Account")
    Test_ATM.Back()
    ATM_Test.Verify(Test_ATM.State, "Insert Card")
    Test_ATM.Back()
    ATM_Test.Verify(Test_ATM.State, "Select Bank")
    Test_ATM.Back()
    ATM_Test.Verify(Test_ATM.State, "Start")

    #Print the final Results
    ATM_Test.PrintResults()



