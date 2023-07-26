"""Задание №6
📌 Доработайте задачу 5.
📌 Вынесите общие свойства и методы классов в класс Животное.
📌 Остальные классы наследуйте от него.
📌 Убедитесь, что в созданные ранее классы внесены правки."""


class Animal:

    def __init__(self, name: str = None, breed: str = 'unknown', age: int = 0):
        self.name = name
        self.breed = breed
        self.age = age

    def print_specific(self):
        return f'Специфические данные'


class Dog(Animal):

    def __init__(self, name: str = None, breed: str = 'unknown', commands: list[str] = 'unknown'):
        super().__init__(name, breed)
        self.commands = commands

    def print_specific(self):
        return f'{self.commands}'


class Fish(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', count_fins: int = 0):
        super().__init__(name, breed)
        self.count_fins = count_fins

    def print_specific(self):
        return f'{self.count_fins}'


class Bird(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', count_flights: int = 0):
        super().__init__(name, breed)
        self.count_flights = count_flights

    def print_specific(self):
        return f'{self.count_flights}'


if __name__ == '__main__':
    dog = Dog('Kat', 'Husky', ['Голос', 'Сидеть'])
    fish = Fish('Nemo', 'Gold Fish', 3)
    bird = Bird('Kesha', 'Попугай', 2)
    animal = Animal('Lexa', 'Cat', 12)
    print(animal.print_specific())
    print(dog.print_specific())
    print(fish.print_specific())
    print(bird.print_specific())
