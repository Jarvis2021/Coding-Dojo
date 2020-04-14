class User:
    def __init__(self, username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, deposit_amount):
        self.account_balance += deposit_amount

    def make_withdrawal(self,withdrawl_amount):
        self.account_balance -= withdrawl_amount

    def display_user_balance(self):
        print("User:", self.name,"," "Balance:", self.account_balance)

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print("User:", self.name,"," "Balance:", self.account_balance)
        print("User:", other_user.name,"," "Balance:", other_user.account_balance)

user1 = User("Pramod", "Pramod.Voola@gmail.com")
user1.make_deposit(1000)
user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(300)
user1.make_withdrawal(650)
user1.display_user_balance()

user2 = User("Joseph", "Joseph@gmail.com")
user2.make_deposit(2000)
user2.make_deposit(800)
user2.make_withdrawal(200)
user2.display_user_balance()

user3 = User("Michael", "Michael@gmail.com")
user3.make_deposit(3000)
user3.make_withdrawal(300)
user3.make_withdrawal(300)
user3.make_withdrawal(300)
user3.display_user_balance()


user1.transfer_money(user3,300)
