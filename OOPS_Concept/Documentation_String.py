class Animal:
    """Represents an animal.

    Attributes:
        name (str): The name of the animal.
        species (str): The species of the animal.
        age (int): The age of the animal.
    """

    def __init__(self, name, species, age):

        self.name = name
        self.species = species
        self.age = age

    def animal_info(self):
        print(f"The Animal name is: {self.name} breed: {self.species} and the age is: {self.age} ")

# Create objects
dog = Animal("Dog", "Buddy", 5)
cat = Animal("Cat", "Whiskers", 3)
bird = Animal("Bird", "Tweety", 1)

cat.animal_info()
bird.animal_info()
dog.animal_info()