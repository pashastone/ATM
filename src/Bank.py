from src.Client import Client
from src.Encrypt import Encrypt
import random

#Class of a Bank that can be accessed via ATM
class Bank:
    def __init__(self, bank_name: str, encryption_key: int):
        #each bank has a unique encryption key to store senative data!
        self.Encryption_key = encryption_key
        self.Name = bank_name
        self.Clients = {}

    #Add Client to bank
    def Add_Client(self, name: str, card_number: str, pin_number: str):
        #Make sure card number is unique, otherwise a random one is generatec
        if self.Clients.get(card_number):
            card_number = self.Get_New_Card_Numer()
        #Encrypt the pin number to protect the client's privacy!
        Encrypted_Card_number=Encrypt(pin_number, self.Encryption_key)
        New_Client = Client(Encrypted_Card_number, card_number, name)
        #Index client in dictionary
        self.Clients[card_number] = New_Client
        return card_number

    #Delete, Get, and List all client APIs
    def Delete_Client(self,card_number: str):
        del self.Clients[card_number]

    def Get_Client(self, card_number: str):
        return self.Clients.get(card_number)

    def Get_All_Clients(self):
        return list(self.Clients.keys())

    #Function to random generate card numbers until card number is unique
    def Get_New_Card_Numer(self):
        Unique_Number_Found = False
        while not Unique_Number_Found:
            new_card_number = str(random.randint(0, 9999999999999999))
            while len(new_card_number) < 16:
                new_card_number = "0" + new_card_number
            if not self.Clients.get(new_card_number):
                Unique_Number_Found = True
        return (new_card_number)

    #Will Check Encrypted Pin Number versus Stored Pin Number
    def Check_Pin(self, card_number: str, pin_number: str):
        if Encrypt(pin_number, self.Encryption_key) ==self.Clients[card_number].Pin:
            return True
        else:
            return False