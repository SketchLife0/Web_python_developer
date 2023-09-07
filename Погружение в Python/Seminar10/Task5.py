from Task6 import Animals


class Fishes(Animals):
    gils = 2

    def get_info(self):
        print(f"Я {self.name}, я рыбка и у меня {self.gils} жабр")


class Birds(Animals):
    wings = 2

    def get_info(self):
        print(f"Я {self.name}, я птичка и у меня {self.wings} крылышек")


class Mammals(Animals):
    paws = 4

    def get_info(self):
        print(f"Я {self.name}, я млекопитающий и у меня {self.paws} лапок")
