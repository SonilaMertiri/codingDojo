class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.age= age
        self.is_rewards_member= False
        self.gold_card_points= 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member:
            print("User already is a member.")
            return False
        else:
            self.is_rewards_member= True
            self.gold_card_points= 200
            print("You are a rewards member and your gold card counts 200 points.")
            return True
        
    def spend_points(self,amount):
        if self.is_rewards_member:
            if self.gold_card_points>= amount:
                self.gold_card_points-= amount
                print("You have spent {amount} gold card points. Your current points are {self.gold_card_points}")
            else:
                print("Your gold card points are less than {amount}.")
        else:
            print("You are not a rewards member. You need to enroll to start earning points.")

user_1= User("Jimin", "Park", "jiminpark@email.com", 28)
user_1.display_info()
user_1.enroll()

user_2= User("Namjoon", "Kim", "namu7@email.com", 29)
user_3= User("Suga", "Min", "minsuga@email.com", 30)

user_1.spend_points(50)
user_2.enroll()
user_2.spend_points(80)

user_2.display_info()
user_3.display_info()
user_3.spend_points(40)