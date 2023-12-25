from bankAccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}     #this is a dictionary when I can store multiple accounts
    
    def add_acount(self, account_id, int_rate=0.02, balance=0):
        new_account= BankAccount(int_rate, balance)
        self.accounts[account_id]= new_account
        print(f"{self.name} you added the account {account_id} with the actual balance of {balance} leke.")
        return new_account
    
    def make_deposit(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].deposit(amount)
            print(f"{self.name} just made a deposite of {amount} leke to account {account_id}.")
        else:
            print(f"This account {account_id} doesn't exist for {self.name}.")
        return self

        # self.account.deposit(amount)
        # print(f"{self.name} just made {amount} leke deposit.")
        # return self
    
    def make_withdraw(self, account_id, amount):
        if account_id in self.accounts:
            self.accounts[account_id].withdraw(amount)
            print(f"{self.name} just made a withdrawal of {amount} leke from account {account_id}.")
        else:
            print(f"This account {account_id} doesn't exist for {self.name}.")
        return self

        # self.account.withdraw(amount)
        # print(f"{self.name} made an {amount} leke withdrow.")
        # return self
    
    def display_user_balance(self, account_id):
        if account_id in self.accounts:
            print(f"\n{self.name} your current balance for account {account_id} is: ")
            self.accounts[account_id].display_account_info()
        else:
            print(f"This account {account_id} doesn't exist for {self.name}.")
        return self

        # print(f"\n{self.name} your current balance is:")
        # self.account.display_account_info()
        # return self

sonila= User("Sonila", "sonila@email.com")
sonila_account1= sonila.add_acount("B1307", int_rate= 0.01, balance= 100)
sonila_account2= sonila.add_acount("A2025", int_rate= 0.02, balance= 200)

sonila.make_deposit("B1307", 70).make_withdraw("A2025", 20)
sonila.display_user_balance("B1307").display_user_balance("A2025")

# sonila.make_deposit(100).make_withdrow(20).display_user_balance()