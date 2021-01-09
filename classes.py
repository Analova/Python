class Car:
     def __init__(self ,maker , model , wheels=4 ,windows=6):
        self.maker=maker,
        self.model=model,
        self.wheels=wheels,
        self.windows=windows,
        self.total=5
        # print(f"Created instance of a car for {maker} {model}")

     def __repr__(self):
        return f"Maker:{self.maker} model:{self.model} wheels:{self. wheels} windows:{self.windows}"


     total=20

     @classmethod
     def testing(cls):
         print("Class ======================")
         print(cls)
         print(cls.total)
         print("Class ======================")


     def printMaker(self):
         print("Instance ======================")
         print(self)
         return self.maker
         print(Car.testing())
         print("Instance ======================")

     def add(self,number):
         Car.total+=number
         self.total+=number
         return f"Class:{Car.total} Instance:{self.total}"




car1=Car("Benz", "ML250")
car2=Car("Benz", "ML250")
car3=Car("BNW", "x6",4,5)
car4=Car("Honda", "Civic Coupe",4,4)

print(car4)


# Claas methods
# print(Car.testing())
# print(car1.printMaker())
# print(car1.testing())

