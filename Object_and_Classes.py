# Object_and_Classes.py

#Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Method
    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

# Objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.show_details()
print()
car2.show_details()
