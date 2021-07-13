class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self,amount):
        self.account_balance-=amount

    def display_user_balance(self):
        print(f"User: {self.name} Balance: ${self.account_balance}")

    def transfer_money(self, another_user, amount):
        another_user.make_deposit(amount)
        self.make_withdrawl(amount)

john = User("John Lennon", "john@gmail.com")
paul = User("Paul McCartney", "paul@gmail.com")
george = User("George Harrison", "george@gmail.com")
ringo = User("Ringo Starr", "ringo@gmail.com")

john.make_deposit(200)
john.make_deposit(200)
john.make_deposit(200)
john.make_withdrawl(100)
john.display_user_balance()

paul.make_deposit(100)
paul.make_deposit(100)
paul.make_deposit(100)
paul.make_withdrawl(50)
paul.display_user_balance()


ringo.make_deposit(300)
ringo.make_deposit(300)
ringo.make_deposit(300)
ringo.make_withdrawl(200)
ringo.display_user_balance()

ringo.transfer_money(paul, 500)
ringo.display_user_balance()
paul.display_user_balance()

# john.display_user_balance()

# paul.make_deposit(500)
# print(john.account_balance)
# print(paul.account_balance)
# george.make_withdrawl(200)
# print(george.account_balance)
# paul.display_user_balance()