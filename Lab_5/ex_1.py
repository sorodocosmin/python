from validator import Validator


class Shape:

    def __init__(self, nr_sides):
        self._nr_of_sides = nr_sides

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    PI = 3.14159

    def __init__(self, radius):
        """
        if radius is not a number, set it to 1
        :param radius:
        """
        super().__init__(0)  # a circle has 0 sides
        if Validator.is_positive_number(radius) is False:
            print("Invalid radius")
            print("Setting radius to 1")
            radius = 1

        self.__radius = radius

    def area(self):
        return Circle.PI * (self.__radius**2)

    def perimeter(self):
        return 2 * Circle.PI * self.__radius

    def diameter(self):
        return 2 * self.__radius


class Rectangle(Shape):
    def __init__(self, length, width):
        """
        if length or width is not a number, set it to 1
        :param length:
        :param width:
        """
        super().__init__(4)

        if Validator.is_positive_number(length) is False or Validator.is_positive_number(width) is False:
            print("Invalid length/width")
            print("Setting length and width to 1")
            length = 1
            width = 1

        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def is_square(self):
        if self.__length == self.__width:
            return True
        return False


class Triangle(Shape):
    def __init__(self, a, b, c):
        """
        if a, b or c is not a number, set it to 3, 4, 5
        :param a:
        :param b:
        :param c:
        """
        super().__init__(3)

        if Validator.can_form_a_triangle(a, b, c) is False:
            print("Invalid numbers")
            print("Setting a, b, c to 3, 4, 5")
            a = 3
            b = 4
            c = 5

        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        # Heron's formula A = sqrt(s(s-a)(s-b)(s-c))
        semi_perimeter = (self.__a + self.__b + self.__c) / 2
        return (semi_perimeter * (semi_perimeter - self.__a) *
                (semi_perimeter - self.__b) * (semi_perimeter - self.__c)) ** 0.5

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def is_right_triangle(self):
        """
        :return: True if the triangle is right, False otherwise
        :return:
        """
        if self.__a**2 + self.__b**2 == self.__c**2:
            return True
        elif self.__a**2 + self.__c**2 == self.__b**2:
            return True
        elif self.__b**2 + self.__c**2 == self.__a**2:
            return True

        return False


# tests
# circle = Circle(5)
# print(circle.area())
# print(circle.perimeter())
#
# rectangle = Rectangle(5, 5)
# print(rectangle.area())
# print(rectangle.perimeter())
# print(rectangle.is_square())
#
triangle = Triangle(1, 0, 1)
print(triangle.perimeter())  # 3+4+5
print(triangle.area())
print(triangle.is_right_triangle())
print(triangle)
