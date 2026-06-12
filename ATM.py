import json
import random
class account:
    def __init__(self):
        self.name=input("Enter your name:- ").strip().lower()
        self.id=random.randint(2103849325,12345876543645575)
        self.acc=f"{self.name}'s_account_{self.id}.json"
        self.pin=int(input("Enter your pin(only in number) of your bank account:- "))
        self.balance=int(input("submite your deposite amount:- "))
        print("your account sucessfully created....")
        self.read={
            "username":self.name,
            "id":self.id,
            "password":self.pin,
            "Balance":self.balance
            }
        self.open=self.read
        with open(self.acc,'w') as f:
            json.dump(self.open,f)
        account_id=self.acc.split('.',1)[0]
        print(f"Notedown Your Account id:\n{account_id}")
class ATM(account):
    def __init__(self):
        self.YN=input('You have bank account? answer in Yes/No:')
        if self.YN=="Yes":
            self.read()
            self.loop()
        else:
            print("Fill Form For Create Bank Account........")
            super().__init__()
            self.loop()
            
    def read(self):
        
        self.acc=input('please enter your account id:')
        self.acc=f"{self.acc}.json"
        with open(self.acc,'r') as self.f:
            self.read=json.load(self.f)
        self.name=self.read["username"]
        self.id=self.read["id"]
        self.pin = self.read["password"]
        self.balance = self.read["Balance"]
    def loop(self):
        while True:
                self.menu()
                if 1 == self.j:
                    self.createpin()
                elif 2 == self.j:
                    self.changepin()
                elif 3 == self.j:
                    self.checkbalance()
                elif 4 == self.j:
                    self.withdraw()
                elif 5 == self.j:
                    self.deposite()
                elif 6 == self.j:
                    self.Transaction()
                else:
                    print("We can recogize your input please try again..")
                    break
    def menu(self):
        self.j=int(input("""
hi how can i help you
1. Press 1 for create pin
2. press 2 for change pin
3. press 3 for check balance
4. press 4 for withdraw
5. press 5 for deposite
6. press 6 for Transaction
 else exit atm:-"""))
    def createpin(self):
        pas=int(input("Enter your pin in here:- "))
        self.pin=pas
        self.update()
        print("your pin sucessfully created")
    def changepin(self):
        a=int(input("Enter your before pin:- "))    
        if a == self.pin:
            print("Your pin is correct")
            self.b=int(input("Enter new pin:- "))
            self.pin=self.b
            self.update()
        else:
            print("wrong pin")
    def checkbalance(self):
        a=int(input("Enter your before pin:- "))
        if a == self.pin:
            print("Your pin is correct")
            print(self.balance)
        else:
            print("wrong pin")
    def withdraw(self):
        a=int(input("Enter your pin:- "))
        if a == self.pin:
            print("Your pin is correct")
            amount=int(input("Enter your amout of withdraw:- "))
            if (amount <= self.balance):
                print("your transaction are complited...")
                self.balance-=amount
                self.update()
            else:
                print("your balance are low then your entered amount please try again..")
        else:
            print("wrong pin")
    def deposite(self):
        a=int(input("Enter your pin:- "))
        if a == self.pin:
            print("Your pin is correct")
            amount=int(input("Enter your amout of deposite:- "))
            self.balance+=amount
            self.update()
            print(f"your amount of {amount} is deposite sucessfully.....")
        else:
            print("wrong pin")
    def update(self):
        self.read["username"]=self.name
        self.read["id"]=self.id
        self.read["password"]=self.pin
        self.read["Balance"]=self.balance
        with open(self.acc,'w') as self.f:
            json.dump(self.read,self.f)
    def Transaction(self):
        self.account=input("Receiver's Account id:")
        self.account = f"{self.account}.json"
        with open(self.account,'r') as self.df:
            read=json.load(self.df)
        recevir_name=read["username"]
        print('recevir_name:',recevir_name)
        transfer=int(input("Enter Your Amout for Transaction:"))
        a=int(input("Enter your pin:"))
        if a == self.pin:
            print("Your pin is correct")
            if (transfer <= self.balance):
                self.balance=self.balance-transfer
                self.update()
                read["Balance"]= read["Balance"]+transfer
                with open(self.account,'w') as f:
                    json.dump(read,f)
                print("your transaction are complited...")
            else:
                print("your balance are low then your entered amount please try again..")
        else:
            print("wrong pin")
k=ATM()