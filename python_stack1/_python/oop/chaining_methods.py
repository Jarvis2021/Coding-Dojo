class User:
    def __init__(self, username,email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, deposit_amount):
        self.account_balance += deposit_amount
        return self

    def make_withdrawal(self,withdrawl_amount):
        self.account_balance -= withdrawl_amount
        return self

    def display_user_balance(self):
        print("User:", self.name,"," "Balance:", self.account_balance)
        return self

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print("User:", self.name,"," "Balance:", self.account_balance)
        print("User:", other_user.name,"," "Balance:", other_user.account_balance)

user1 = User("Pramod", "Pramod.Voola@gmail.com")
user1.make_deposit(1000).make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(650).display_user_balance()

user2 = User("Joseph", "Joseph@gmail.com")
user2.make_deposit(2000).make_deposit(800).make_withdrawal(200).display_user_balance()

user3 = User("Michael", "Michael@gmail.com")
user3.make_deposit(3000).make_withdrawal(300).make_withdrawal(300).make_withdrawal(300).display_user_balance()


user1.transfer_money(user3,300)
