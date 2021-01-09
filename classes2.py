class Vehicle:
    def __init__(self,wheels,windows,seat):
        self.wheels=wheels
        self.windows=windows
        self.seats=seat
    
    def printWheels(self):
        print(f"This vehicles has {self.wheels} wheels")
        return self.wheels

class Car(Vehicle):
    def __init__(self,model,maker,wheels,windows,seats):
        super().__init__(wheels,windows,seats)
        self.model=model
        self.maker=maker

    def __repr__(self):
        return f"This is a car by {self.maker} with wheels:{self.wheels}"

class Motor(Vehicle):
    def __init__(self,model,maker,wheels,windows,seats):
        super().__init__(wheels,windows,seats)
        self.model=model
        self.maker=maker

    def __repr__(self):
        return f"This is a Motorcycle by {self.maker}"


car1=Car( "GL359","Benz", 4, 6,5)
motor1=Motor("SP1000", "BMW", 2, 1,2)

# print(car1.printWheels())
# print(motor1.printWheels())
print(car1)
