class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self,amount):
        self.account_balance-=amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name} Balance: ${self.account_balance}")
        return self

    def transfer_money(self, another_user, amount):
        another_user.make_deposit(amount)
        self.make_withdrawl(amount)
        return self

john = User("John Lennon", "john@gmail.com")
paul = User("Paul McCartney", "paul@gmail.com")
george = User("George Harrison", "george@gmail.com")
ringo = User("Ringo Starr", "ringo@gmail.com")

john.make_deposit(200).make_deposit(200).make_deposit(200).make_withdrawl(100).display_user_balance()

paul.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawl(50).display_user_balance()

ringo.make_deposit(300).make_deposit(300).make_deposit(300).make_withdrawl(200).display_user_balance()

# ringo.transfer_money(paul, 500)
# ringo.display_user_balance()
# paul.display_user_balance()