class Animals:
    alive = True
    name = ''

    def __init__(self, name: str):
        self.name = name

    def sey_hello(self):
        if self.alive:
            print(f"Привет! Меня зовут {self.name}")

    def __str__(self):
        return "Я родился!"
