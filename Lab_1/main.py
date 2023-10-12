def gcd(a,b):
    """
        Finds the gcm from 2 numbers
    """
    while (a % b) != 0:
        r = a % b
        a = b
        b = r

    return b


def ex_1():
    """
        Find the greatest common divisor from numbers read from the console
        until the numbers 0 is read
    """
    print(gcd(24,12))


def ex_2(message):
    """
    :param message:
    :return: the number of vowels in message
    """
    nr = 0
    print(message)
    for char in message:
        if char in "aeiouAEIOU" :
            nr += 1

    return nr


def ex_3(string, substring):
    """

    :param string:
    :param substring:
    :return: the number of substring in string
    """
    nr = 0
    while substring in string:
        string.replace(substring, "")
        nr += 1

    return nr
    #  return len(string.split(substring))-1


def ex_4(string):
    """
    :param string:
    :return: from UpperCamelCase string into lowercase_with_underscore
    """
    for char in string:

        if char.isupper():
            string.r

    return string

print(ex_2("buna ziua ae O LL 0 OO"))
print(ex_3("hellohelloshello hello hello","hello"))
print(ex_4("heEllO"))
