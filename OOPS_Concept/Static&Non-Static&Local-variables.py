class Car:
    # Static variable (class variable), shared by all instances
    total_cars = 0

    def __init__(self, brand, model, color):
        # Non-static (instance) variables, unique to each instance
        self.brand = brand
        self.model = model
        self.color = color

        # Modify static variable, every time a car is created
        Car.total_cars += 1
    
    def display_info(self):
        # Local variable, only accessible within this method
        local_message = f"Car Information: {self.brand} {self.model} {self.color}"
        print(local_message)  # Using the local variable

    @staticmethod
    def display_total_cars():
        # Static method accessing the static variable
        print(f"Total cars created: {Car.total_cars}")

# Creating instances of Car
car1 = Car("Toyota", "Camry", "Red")
car2 = Car("Honda", "Civic", "Blue")

# Displaying information for car1 and car2
car1.display_info()  # Output: Car Information: Toyota Camry Red
car2.display_info()  # Output: Car Information: Honda Civic Blue

# Accessing the static variable (same for all instances)
Car.display_total_cars()  # Output: Total cars created: 2
