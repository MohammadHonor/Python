import sys
class custumar:
    '''Bank related application'''
    bankname='HONOURBANK'
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance + amount
        print("Current balance in your acount:",self.balance)
    def withdraw(self,amount):
        if self.amount > self.balance:
            print("Insufficent balance  in your acount")
            sys.exit()
        else:
            self.balance=self.balance - self.amount
            print("Your remaining balance in your account",self.balance)
print("THIS IS BANK INTERFACE")
n=input('Enter your name:')
print('WELCOM TO ',custumar.bankname)
b=custumar(n)
while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option=input("Select your choice:")
    if option=='d' or option=='D':
        amount=float(input("Enter Amount:"))
        b.deposit(amount)
    elif option=='w' or option=='W':
        amount=float(input('Enter Amount:'))
        b.withdraw(amount)
    elif option=='e' or option=='E':
        print('Thanks for visting ',custumar.bankname)
        sys.exit()
    else:
        print('Select Correct Option')



