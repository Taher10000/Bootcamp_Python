import re


class Phone:
    def __init__(self,color, weight):
        self.color = color
        self.weight = weight

    def info(self):
        print(f"color: {self.color}")
        print(f"weight: {self.weight}")
        return self

    def call(self, number):
        print(f"calling {number}")
        return self

    def ring(self):
        print("ringing ringing ringing")
        return self

    def hang_up(self):
        print("hanging up")
        return self

class CellPhone(Phone):
    def __init__(self, color, weight):
        super().__init__(color, weight)
        self.type = "Cell Phone"
        
    def info(self):
        super().info()
        print(f"type: {self.type}")
        return self
    def text(self,number,msg):
        print(f"Sending number {number} message {msg}")
        return self
class FlipCellPhone(CellPhone):
    def __init__(self, color, weight):
        super().__init__(color, weight)
        self.flip_status = "close"
        self.type = "Flip Cell Phone"
    def info(self):
        super().info()
        return self
    def flipped_closed(self):
        self.flipped_status = "closed"
        return self
    def flipped_open(self):
        self.flipped_status = "open"
        return self
    def call(self, number):
        if self.flip_status == "closed":
            print("must open phone first")
        else:
            super().call(number)
        return self



phone1 = FlipCellPhone("silver", 5)

phone1.info().flipped_open().call(1234456677).text(1234456677, "Just sending a msg")
