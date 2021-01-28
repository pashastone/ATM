ATM API by Pasha Stone

My API for an ATM Consists of the Following Classes (all in the src folder):

Accounts: Object to hold one bank account and it's information

Client: Object to store bank information and holds accounts of clients. Can add, delete, and list bank accounts. Accounts can be looked up by their assigned name.

Bank: Object to hold all clients of a bank, and also add, delete, and list current clients. Clients can be looked up by their debit card number. All PIN numbers are stored after being run through the encryption API, and PIN numbers can be encrypted and compared, but not unencrypted.

ATM, which interfaces with multiple banks. ATM contains both an API for editing which banks are on the ATM, as well as being an interface for using the ATM. You can select options with the "Select" function within the class, insert your debit with the "Insert Card" function (Make sure it's a 16 digit string), enter your pin (4 digit string) or withdrawal amount with the "Number_Entered" function, and lastly you can put cash into the machine with the "Insert_Cash" function. All current options available on the ATM can be displayed with the "Display_Options" function.

My Test Bench (root folder):

I implemented a small test class that can compare values and record test results. To run my test bench, simply run the Unit_Test.py file (I have version 3.7.1) and the expected result is the following:

Encryption Test: 3/3 Test Cases Passed
Account Test: 6/6 Test Cases Passed
Bank Test: 6/6 Test Cases Passed
ATM Test: 31/31 Test Cases Passed

Please refer to the comments in Unit_Test.py for explanation on what each test is doing