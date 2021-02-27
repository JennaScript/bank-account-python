from random import randint

class BankAccount:
    account_number = randint(0,99999999)
    routing_number = 123456789
    balance = 0

    def __init__(self, full_name):
        self.full_name = full_name
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nAmount Deposited: {round(amount, 2)}")
        return
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            print("\nInsufficient funds. You have been charged an overdraft fee")
            self.balance = self.balance + amount - 10 #adds withdraw back to account and adds a 10 dollar overdraft fee
            return
        print(f"\nAmount Withdrawn: {round(amount, 2)}")
        return
    def get_balance(self):
        print(f"\nYou currently have ${round(self.balance, 2)}")
        return self.balance
    def add_interest(self):
        interest = self.balance *  0.00083
        self.balance = self.balance + interest
        return
    def print_receipt(self):
        print(f"\n{self.full_name}\nAccount No.: {self.account_number} \nRouting No.: {self.routing_number}\nBalance: ${round(self.balance, 2)}")

jennalyn_account = BankAccount("Jennalyn Kabiling")
disney_account = BankAccount("Walt Disney")
rowling_account = BankAccount("J.K Rowling")

jennalyn_account.deposit(100)
jennalyn_account.print_receipt()

jennalyn_account.add_interest()
jennalyn_account.print_receipt()

jennalyn_account.withdraw(1000)
jennalyn_account.print_receipt()