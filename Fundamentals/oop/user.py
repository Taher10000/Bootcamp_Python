class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"Fullname: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Membership: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

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

taher.enroll()
taher.spend_points(50)
taher.display_info()

alex = User('Alex','Robbins','alexrobbins@mail.com',25)
steve = User('Steve','Jobz','stevejobz@apples.com',30)
alex.enroll()
alex.spend_points(80)
alex.display_info()
# steve.display_info()
taher.enroll()
steve.enroll()
steve.spend_points(210)
steve.display_info()


