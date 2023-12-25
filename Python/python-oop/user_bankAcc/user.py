from bankAccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f"{self.name} just made {amount} leke deposit.")
        return self
    
    def make_withdrow(self,amount):
        self.account.withdraw(amount)
        print(f"{self.name} made an {amount} leke withdrow.")
        return self
    
    def display_user_balance(self):
        print(f"\n{self.name} your current balance is:")
        self.account.display_account_info()
        return self

sonila= User("Sonila", "sonila@email.com")
# sonila.account.deposit(50)

sonila.make_deposit(100).make_withdrow(20).display_user_balance()