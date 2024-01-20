class Cars:
    def __init__(self, name, type, purchase, year):
        self.name = name
        self.type = type
        self.purchase = purchase
        self.year = year

    def Model(self):
        print(f"{self.name}")
    def Make(self, year):
        print(f"{self.name} is a {self.type}")
    def Cost(self,purchase):
        print(f"{self.name} was purchased at {self.purchase}")


car_1 = Cars("Ford Mustang", "Truck", "$24,000", "1970")
car_2 = Cars("Bentley", "Car", "$84,000","1971")

car_1.Model()
car_1.Make("Truck")
car_1.Cost("$24,000")

car_2.Model()
car_2.Make("Car")
car_2.Cost("84,000")
