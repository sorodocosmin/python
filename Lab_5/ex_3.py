from datetime import datetime


class Vehicle:
    def __init__(self, make, model, year, nr_of_wheels, kg):
        self._make = make
        self._model = model
        self._year = year
        self._nr_of_wheels = nr_of_wheels
        self._mass_in_kg = kg

    def get_approx_mileage(self):
        pass

    def get_towing_capacity(self):
        pass

    def get_nr_of_wheels(self):
        return self._nr_of_wheels


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, kg):
        super().__init__(make, model, year, 2, kg)

    def get_approx_mileage(self):
        """
        on average a motorcycle milage is around 3k on year
        :return:
        """
        return (datetime.now().year - self._year) * 3_000

    def get_towing_capacity(self):
        return self._mass_in_kg * 0.5




class Car(Vehicle):
    def __init__(self, make, model, year, kg):
        super().__init__(make, model, year, 4, kg)

    def get_approx_mileage(self):
        """
        on average a car milage is around 10k on year
        :return:
        """
        return (datetime.now().year - self._year) * 12_000

    def get_towing_capacity(self):
        return self._mass_in_kg * 0.85


class Truck(Vehicle):
    def __init__(self, make, model, year, kg):
        super().__init__(make, model, year, 8, kg)

    def get_approx_mileage(self):
        """
        on average a truck milage is around 60k on year
        :return:
        """
        return (datetime.now().year - self._year) * 60_000

    def get_towing_capacity(self):
        return self._mass_in_kg * 2.5


# tests

# car = Car("Ford", "Focus", 2010, 3_500)
# print(car.get_approx_mileage())
# truck = Truck("Volvo", "FH", 2015)
# print(truck.get_approx_mileage())
# motorcycle = Motorcycle("Honda", "CBR", 2019, 400)
