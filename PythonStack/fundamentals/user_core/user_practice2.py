class User:
    
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0
    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name} , Balance: $ {self.account_balance}")
    
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)
richard = User("Richard", "richy@codingdojo.com")
emily = User("Emily", "emily@codingdojo.com")
yeesa = User("Yeesa", "yeesa@codingdojo.com")

richard.make_deposit(100).make_deposit(110).make_deposit(120).make_withdraw(30).display_user_balance()

emily.make_deposit(70).make_deposit(90).make_withdraw(45).make_withdraw(55).display_user_balance()

yeesa.make_deposit(850).make_withdraw(105).make_withdraw(115).make_withdraw(125).display_user_balance()

yeesa.transfer_money(emily, 50)
yeesa.display_user_balance()
emily.display_user_balance()