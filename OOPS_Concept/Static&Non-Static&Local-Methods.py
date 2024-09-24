class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    # Non-static (Instance) Method
    def show_car_details(self):
        # Local method (defined inside another method)
        def get_engine_type():
            return 'V8'
        
        print(f"Car make: {self.make}, Model: {self.model}")
        print(f"Engine type: {get_engine_type()}")  # Calling local method

    # Static Method (belongs to the class, not instances)
    @staticmethod
    def show_wheels():
        # Static methods can't access instance variables directly
        print(f"All cars have {Car.wheels} wheels.")
    
    # Class Method (another type of static method, operates on the class level)
    @classmethod
    def show_class_info(cls):
        print(f"This is the Car class, and all cars have {cls.wheels} wheels.")
    

# Creating an instance of Car
car1 = Car('Toyota', 'Corolla')

# Calling instance (non-static) method
car1.show_car_details()

# Calling static method (can be called on the class or an instance)
Car.show_wheels()

# Calling class method (operates on class level)
Car.show_class_info()
