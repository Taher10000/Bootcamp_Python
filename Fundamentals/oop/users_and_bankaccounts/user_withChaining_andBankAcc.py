from bank_acc import BankAccount
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(int_rate = 0.2,balance = 0)
        self.savings = BankAccount()
        self.checkings = BankAccount()

    def make_deposit(self, accType,amount):
        if accType == "savings":
            self.savings.deposit(amount)
        if accType == "checkings":
            self.checkings.deposit(amount)
        return self

    def make_withdraw(self):
        self.account.withdraw(100)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    # def transfer_money(self,amount,other_user):
    #     self.account.withdraw(amount)
    #     other_user.account.deposit(amount)

    def display_info(self):
        print(f"Fullname: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Membership: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
        print(f"Savings: {self.savings.balance}")
        print(f"Checkings: {self.checkings.balance}")
        print("\n")

        return self

    def enroll(self):
        if self.is_rewards_member:
            print(f"You are already a member {self.first_name}")
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"NOT ENOUGH GOLD POINTS {self.first_name}.")
            return self
        else:
            self.gold_card_points -= amount
            return self

taher = User('Taher','Mac','tm000@tmail.com', 23)
taher.enroll().spend_points(50).enroll().display_info().make_deposit("savings",200).make_deposit("checkings",100).display_info()

alex = User('Alex','Robbins','alexrobbins@mail.com',25)
alex.enroll().spend_points(80).display_info()

steve = User('Steve','Jobz','stevejobz@apples.com',30)
steve.enroll().spend_points(210).display_info()


