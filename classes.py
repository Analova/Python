class Car:
     def __init__(self ,maker , model , wheels=4 ,windows=6):
        self.maker=maker,
        self.model=model,
        self.wheels=wheels,
        self.windows=windows,
        print(f"Created instance of a car for {maker} {model}")


car1=Car("Benz", "ML250")
car2=Car("Benz", "ML250")
car3=Car("BNW", "x6",4,5)
car4=Car("Honda", "Civic Coupe",4,4)



