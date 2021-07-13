class BankAccount:

        # don't forget to add some default values for these parameters!
        def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
                self.int_rate = int_rate
                self.balance = balance
        
        def deposit(self, amount):
        # your code here
                self.balance += amount
                return self
        
        def withdraw(self, amount):
        # your code here
                if amount > self.balance:
                        print("Insufficient funds: Charging a $5 fee")
                        self.balance -= 5
                else:
                        self.balance -= amount
                return self
        def display_account_info(self):
        # your code here
                print("Balance $" + str(self.balance))
                
        def yield_interest(self):
        # your code here
                if self.balance > 0:
                        self.balance += self.balance * self.int_rate
                return self      
richard = BankAccount(0.1, 500)
yeesa = BankAccount(0.1, 800)

richard.deposit(150).deposit(200).deposit(40).withdraw(430).yield_interest().display_account_info()

yeesa.deposit(130).deposit(160).withdraw(30).withdraw(55).withdraw(270).withdraw(245).yield_interest().display_account_info()
