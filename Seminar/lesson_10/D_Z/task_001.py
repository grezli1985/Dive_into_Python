from Seminar.lesson_10.task_6 import Dog, Bird, Fish, Animal


class AnimalsCreator(Dog, Bird, Fish, Animal):

    @staticmethod
    def create_animal(name: str, breed: str, age: int):
        return Animal(name, breed, age)

    @staticmethod
    def create_bird(name: str, breed: str, count_flights: int):
        return Bird(name, breed, count_flights)

    @staticmethod
    def create_dog(name: str, breed: str, commands: list[str]):
        return Dog(name, breed, commands)

    @staticmethod
    def create_fish(name: str, breed: str, count_fins: int):
        return Fish(name, breed, count_fins)
    #
    # def __repr__(self):
    #     return f'AnimalsCreator({self.name}, {self.breed}, {self.count_fins})'


if __name__ == '__main__':
    dog = AnimalsCreator.create_dog('Gav-gav', 'Husky', ['Голос', 'Сидеть'])
    print(dog.name)
    fish = AnimalsCreator.create_fish('Fish', 'Gold Fish', 3)
    print(fish.name)
    animal = AnimalsCreator.create_animal('!!!!', '???', 4)
    print(animal.name)
