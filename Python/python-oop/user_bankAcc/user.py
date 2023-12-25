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
    
    
    # Add a transfer_money(self, amount, other_user)
    # method to the user class that takes an amount and a different User instance,
    # and transfers money from the user's account into another user's account.

    def transfer_money(self, amount, other_user, from_account_id, to_account_id):
        if from_account_id in self.accounts and to_account_id in other_user.accounts:
            if self.accounts[from_account_id].balance>= amount:
                self.accounts[from_account_id].withdraw(amount)
                other_user.accounts[to_account_id].deposit(amount)
                print(f"{self.name} transferred {amount} from account {from_account_id} to {other_user.name} account {to_account_id}.")
            else:
                print(f"Transfer failed. Insufficient funds from {self.name} with account {from_account_id}")
        else:
            print("Unknown account information. Transfer failed.")
        return self
    
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
sonila_account1= sonila.add_acount("sonila1", int_rate= 0.01, balance= 100)
sonila_account2= sonila.add_acount("sonila2", int_rate= 0.02, balance= 200)

sonila.make_deposit("sonila1", 70).make_withdraw("sonila2", 20)
sonila.display_user_balance("sonila1").display_user_balance("sonila2")

# sonila.make_deposit(100).make_withdrow(20).display_user_balance()

paola= User("Paola", "paola@email.com")
paola_account1= paola.add_acount("paola1", int_rate= 0.02, balance= 300)
sonila.transfer_money(30, paola, "sonila2", "paola1")
sonila.display_user_balance("sonila2").display_user_balance("sonila1")
paola.display_user_balance("paola1")