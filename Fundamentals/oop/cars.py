class Car:
    creator = "Taher"
    def __init__(self,make, model='rav4',color='blue'):
        self.make = make
        self.model = model
        self.color = color
        self.is_running = False

    def info(self):
        print("*"*50)
        print(f"make: {self.make}")
        print(f"color: {self.color}")
        print(f"creator: {self.creator}")

    def turn_on(self):
        self.is_running = True
    
    def drive(self):
        if self.is_running:
            print("driving rrrrr")
        else:
            print("not on, cant drive")
    
    @classmethod
    def change_creator(cls,new_creator):
        cls.creator = new_creator

    @staticmethod
    def appropriate_color(color):
        color_list = ['blue','black','white']
        if color in color_list:
            return True
        else:
            return False



car_a = Car("toyota","rav4","blue")
car_b = Car("tesla","model4","red")
car_a.turn_on()

Car.change_creator("Mac")
print(appropriate_color(car_b(color)))
car_b.info()
print("Hello World")
print(car_a.color)
car_a.drive()
car_a.info()