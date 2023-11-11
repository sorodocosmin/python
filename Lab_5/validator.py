class Validator:
    @staticmethod
    def is_positive_number(number):
        """
        :param number:
        :return:  True if number is a positive number, False otherwise
        """
        if type(number) is not int and type(number) is not float:
            return False
        elif number <= 0:
            return False

        return True

    @staticmethod
    def can_form_a_triangle(a, b, c):
        """
        :param a:
        :param b:
        :param c:
        :return: True if a, b, c can form a triangle, False otherwise
        """
        if Validator.is_positive_number(a) is False or Validator.is_positive_number(b) is False or Validator.is_positive_number(c) is False:
            return False
        elif a + b <= c or a + c <= b or b + c <= a:
            return False

        return True
