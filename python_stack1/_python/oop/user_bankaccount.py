class User:
    def __init__(self, username,email_address, bank_account):
        self.name = username
        self.email = email_address
        self.account = bank_account


    # def transfer_money(self,other_user,amount):
    #     self.account.balance -= amount
    #     other_user.account_balance += amount
    #     print("User:", self.name,"," "Balance:", self.account.balance)
    #     print("User:", other_user.name,"," "Balance:", other_user.account_balance)


class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest_rate = float(int_rate/100)
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdrwal(self,amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -=5
            print("Insufficient funds: Charging a $5 fee", self.balance)
        else:
            self.balance
        return self
    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance < 0:
            print("There is no Interest Earned on Negative Balance:", self.balance)
        elif self.balance > 0:
            interest_amount = self.interest_rate * self.balance
            print("Interest Yielded:", interest_amount)
            self.balance += interest_amount
            print("Balance:", self.balance)
        return self


account1 = BankAccount(2,0)
account2 = BankAccount(3,0)

user1 = User("Pramod", "Pramod.Voola@gmail.com", account1)
user1.account.deposit(1000).deposit(100).deposit(200).deposit(350).withdrwal(650).display_account_info().yield_interest()

user1 = User("Pramod", "Pramod.Voola@gmail.com", account2)
user1.account.deposit(1000).deposit(100).deposit(200).deposit(350).withdrwal(2650).display_account_info().yield_interest()
