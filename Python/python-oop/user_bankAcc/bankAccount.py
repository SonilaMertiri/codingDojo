class BankAccount:
    transaction_fee= 5
    all_accounts = []

    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate= int_rate
        self.balance= balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance+= amount
        print(f"Your deposite is {amount} it means that your balance already is {self.balance}")
        return self
    
    def withdraw(self, amount):
        if amount<= self.balance:
            self.balance-=amount
            print(f"Your withdraw is {amount}. Your current balance is {self.balance}")
        else:
            print(f"Insuficient funds, this will charge you {self.transaction_fee}")
            self.balance-= self.transaction_fee
        return self

    def display_account_info(self):
        print("\nYour account information:")
        print(f"Balance: {self.balance}")
        print(f"Interest rate: {self.int_rate} \n")
        return self
    
    def yield_interest(self):
        if self.balance> 0:
            interes_earned= self.balance* self.int_rate
            self.balance+= interes_earned
            print(f"Your balance already is {self.balance} due to your erned interest by {self.int_rate}.")
        else:
            print("Your balance is negative. No interest earned.")
        return self
    
# # use a classmethod to print all instances of a Bank Account's info
#     @classmethod
#     def print_all_accounts(cls):
#         for account in cls.all_accounts:
#             account.display_account_info()
#         return cls
    
# user1= BankAccount(0.02,50)
# user1.deposit(20).deposit(10).deposit(30).withdraw(5).yield_interest().display_account_info()

# user2= BankAccount(0.05,100)
# user2.deposit(10).deposit(100).withdraw(20).withdraw(10).withdraw(15).withdraw(50).yield_interest().display_account_info()

# BankAccount.print_all_accounts()