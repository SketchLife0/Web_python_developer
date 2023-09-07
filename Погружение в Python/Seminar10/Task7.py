from Task5 import *


class Factory:
    animals = {
        "млекопитающее": Mammals,
        "птица": Birds,
        "рыба": Fishes,
    }

    def __init__(self, type_animal: str, *args, **kwargs):
        animal = self.animals.get(type_animal.lower(), None)
        if animal:
            print(animal(*args, **kwargs))
        else:
            print("Таких животных нет")


Factory("ПТИца", 'asdf')
Factory("ПТИа", 'asdf')
