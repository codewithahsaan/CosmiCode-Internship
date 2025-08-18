# Base Class
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

    def start_engine(self):
        return "Engine started."


# Derived Class - Car
class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def display_info(self):
        return f"Car: {super().display_info()}, Doors: {self.doors}"


# Derived Class - Bike
class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type  # e.g., Sports, Cruiser

    def display_info(self):
        return f"Bike: {super().display_info()}, Type: {self.bike_type}"


# Example Usage
car = Car("Toyota", "Corolla", 2022, 4)
bike = Bike("Yamaha", "R15", 2021, "Sports")

print(car.display_info())
print(car.start_engine())

print(bike.display_info())
print(bike.start_engine())

