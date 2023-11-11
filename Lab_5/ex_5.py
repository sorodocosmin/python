class Animal:
    def __init__(self, name, number_of_legs):
        self._name = name
        self._number_of_legs = number_of_legs

    def can_fly(self):
        pass

    def can_swim(self):
        pass


class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name, 4)

    def can_fly(self):
        return False

    def can_swim(self):
        return False


class Bird(Animal):
    def __init__(self, name, migrates):
        super().__init__(name, 2)
        self.__migrates = migrates

    def can_fly(self):
        return True

    def can_swim(self):
        return False

    def migrates_during_winter(self):
        return self.__migrates


class Fish(Animal):
    def __init__(self, name):
        super().__init__(name, 0)

    def can_fly(self):
        return False

    def can_swim(self):
        return True
