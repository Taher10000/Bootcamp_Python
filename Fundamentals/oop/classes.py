

class Person:
    def __init__(self,first_name,last_name,height,weight,age,shoe_size):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.weight = weight
        self.age = age
        self.shoe_size = shoe_size
        self.shoes = []
        self.km = 0
        self.fullname = f"{first_name} {last_name}"

    def info(self):
        print(f"fullname: {self.fullname}")
        print(f"height: {self.height}")
        print(f"weight: {self.weight}")
        print(f"age: {self.age}")
        print(f"shoe size: {self.shoe_size}")

        print("*"*80)
        return self
    def shoes_info(self):
        for index, shoe in enumerate(self.shoe):
            print("^"*80)
            print(f"Shoe number: {index+1}")
            shoe.info()
            print("^"*80)
        return self

    def walk(self):
        distance = int(input)
        print("Your shoes...")
        self.shoes_info()
        self.km += distance



    def get_shoes(self,shoe):
        if shoe.size != self.shoe_size:
            print("You cant have that shoe")
            return self
        self.shoes.append(shoe)
        print("you have a new shoe")
        return self


class Shoe:
    def __init__(self,brand,color,type,size):
        self.brand = brand
        self.color = color
        self.type = type
        self.size = size 
        self.km = 0

    def info(self):
        print(f"brand: {self.brand}")
        print(f"color: {self.color}")
        print(f"Km: {self.km}")


p1 = Person('Taher', 'Mac',160,60,22,9)
s1 = Shoe('Nike','red','running',10)
s2 = Shoe('Nike','red','running',9)
s3 = s2 = Shoe('Adidas','green','running',9)

is_playing = True

p1.get_shoes(s2).get_shoes(s3)
while (is_playing = False)


p1.info()