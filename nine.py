# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    def __init__(self,name) -> None:
        self.name = name
class Pets(Animals):
    def __init__(self, name, species) -> None:
        self.species = species
        super().__init__(name)
class Dog(Pets):
    def __init__(self, name, breed) -> None:
        self.breed = breed
        super().__init__(name, 'Dog')
    def bark(self):
        print(f'Bark! Bark! Barakie! Bark! Bark! little {self.name} Bark!')

a = Dog('Bruno', 'Chihuahua')
a.bark()