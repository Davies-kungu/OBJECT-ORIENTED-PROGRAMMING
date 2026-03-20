class Car:
    def __init__(self, brand="Unknown", year=0):
        if year < 0:
            raise ValueError("Year cannot be negative")
        self.brand = brand
        self.year = year

    @classmethod
    def from_string(cls, data):
        brand, year = data.split(",")
        return cls(brand, int(year))

    def __str__(self):
        return f"Car brand: {self.brand}, Year: {self.year}"

    def __del__(self):
        print(self.brand, "object destroyed")


print("Default constructor:")
car1 = Car()
print(car1)

print("\nParameterized constructor:")
car2 = Car("Toyota", 2020)
print(car2)

print("\nAlternative constructor:")
car3 = Car.from_string("Honda,2022")
print(car3)

print("\nInput validation test:")
try:
    car4 = Car("BMW", -1)
except ValueError as e:
    print("Error:", e)
del car2
