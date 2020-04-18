class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest_rate = float(int_rate/100)
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
        print(self.balance)
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
            print("Negative Balance:", self.balance)
        elif self.balance > 0:
            interest_amount = self.interest_rate * self.balance
            print("Interest Yielded:", interest_amount)
            self.balance += interest_amount
            print("Balance:", self.balance)
        return self


account1 = BankAccount(2,0)
account2 = BankAccount(3,0)

# account1.deposit(1000).deposit(500).deposit(500).withdrwal(200).display_account_info().yield_interest()
account1.deposit(500).deposit(1500).withdrwal(1100).display_account_info().yield_interest()

# .withdrwal(1000).display_account_info().yield_interest()
