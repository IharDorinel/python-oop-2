import pickle
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} roars")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} sings")

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} screams")

tiger = Mammal('Tigra', 5)
robin = Bird('Robin', 2)
gecco = Reptile('Gecco', 3)

creatures = [tiger, robin, gecco]

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

animal_sound(creatures)

class Employee():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ZooKeeper(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)

    def feed_animal(self, animal):
        print(f"{animal.name} покормлен")

class Veterinarian(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)

    def heal_animal(self, animal):
        print(f"{animal.name} вылечен")


ron = Employee('Ron', 25)
albert = ZooKeeper('Albert', 31)

class Zoo():
    def __init__(self):
        self.animals = []
        self.veterinarian = Veterinarian('Rodrigo', 35)
        self.employees = [self.veterinarian]

    def get_info_animals(self):
        with open('animals.pkl', 'rb') as file:
            animals = pickle.load(file)
            for animal in animals:
                print(animal.name)

    def get_info_employees(self):
        with open('employees.pkl', 'rb') as file:
            employees = pickle.load(file)
            for employee in employees:
                print(employee.name)

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в фонд")
        with open('animals.pkl', 'wb') as file:
            pickle.dump(self.animals, file)

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.name} добавлен в штат")
        with open('employees.pkl', 'wb') as file:
            pickle.dump(self.employees, file)

zoo = Zoo()
zoo.add_animal(tiger)
zoo.add_animal(robin)
zoo.add_animal(gecco)
zoo.add_employee(ron)
zoo.add_employee(albert)
zoo.get_info_animals()
zoo.get_info_employees()
albert.feed_animal(tiger)
zoo.veterinarian.heal_animal(gecco)