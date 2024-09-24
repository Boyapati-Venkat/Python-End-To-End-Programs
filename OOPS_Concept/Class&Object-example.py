class Car:
    def __init__(self, make, model, year):
        self.make = make        # Initializes the make attribute
        self.model = model      # Initializes the model attribute
        self.year = year        # Initializes the year attribute
    
    def display_info(self):     # Method to display car information
        print(f"Car: {self.year} {self.make} {self.model}")


        
# Creating an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Displaying the car information
my_car.display_info()
