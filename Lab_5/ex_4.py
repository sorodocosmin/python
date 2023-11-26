class Employee:
    def __init__(self, name, salary, age):
        self._name = name
        self._salary = salary
        self._age = age

    def get_bonus(self):
        pass


class Manager(Employee):
    def __init__(self, name, salary, age, nr_of_subordinates):
        super().__init__(name, salary, age)
        self._nr_of_subordinates = nr_of_subordinates
        self._list_of_subordinates = []

    def get_bonus(self):
        return self._salary * 0.15

    def add_subordinate(self, employee, required_programming_language):
        if employee.knows_programming_language(required_programming_language):
            self._list_of_subordinates.append(employee)
            return True
        return False


class Engineer(Employee):
    def __init__(self, name, salary, age, nr_of_projects):
        super().__init__(name, salary, age)
        self.__nr_of_projects = nr_of_projects
        self.__programming_language = []
        self.__projects_finished = 0

    def get_bonus(self):
        return self._salary * (self.__projects_finished / self.__nr_of_projects) * 0.5

    def add_programming_language(self, language):
        self.__programming_language.append(language)

    def knows_programming_language(self, language):
        return language in self.__programming_language

    def finish_project(self):
        self.__projects_finished += 1


class SalesPerson(Employee):
    def __init__(self, name, salary, age, nr_of_clients):
        super().__init__(name, salary, age)
        self.__nr_of_clients = nr_of_clients
        self.__nr_of_sales = 0

    def get_bonus(self):
        return self._salary * (self.__nr_of_sales/self.__nr_of_clients) * 0.5

    def make_sale(self):
        self.__nr_of_sales += 1
        