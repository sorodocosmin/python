def gcd(a, b):
    """
        Finds the gcd of 2 numbers
    """
    while b != 0:
        r = a % b
        a = b
        b = r

    return b


def ex_1():
    """
        Find the greatest common divisor of n numbers read from the console
    :return: the gcd of all numbers, if one of them is 0 it returns -1
    """
    n = int(input("The number of numbers n= "))
    if n < 2:
        print("n needs to be > 2")
        return -1

    a = int(input("nr1= "))
    b = int(input("nr2= "))

    if a == 0 or b == 0:
        print("nr cannot be 0")
        return -1

    r = gcd(a, b)
    for i in range(3, n):
        a = int(input("nr" + str(i)))
        if a == 0:
            print("nr cannot be 0")
            return -1
        r = gcd(a, r)

    return r


def ex_2(message):
    """
    :param message:
    :return: the number of vowels in message
    """
    nr = 0
    for char in message:
        if char in "aeiouAEIOU":
            nr += 1

    return nr


def ex_3(string, substring):
    """
    :param string:
    :param substring:
    :return: the number of substring in string
    """
    if substring == "":
        return None

    ct = 0

    for i in range(len(string)):
        if string[i] == substring[0]:
            j_string = i
            j_substring = 0
            nr = 0
            while j_string < len(string) and j_substring < len(substring):
                if string[j_string] == substring[j_substring]:
                    nr += 1
                else:
                    break
                j_string += 1
                j_substring += 1

            if nr == len(substring):
                ct += 1

    return ct


    #  return len(string.split(substring))-1


def ex_4(upperCamelCase):
    """
    :param upperCamelCase:
    :return: from UpperCamelCase string into lowercase_with_underscore
    """
    lowercase_with_underscores = ""
    for char in upperCamelCase:
        if char.isupper():
            lowercase_with_underscores += "_" + char.lower()
        else:
            lowercase_with_underscores += char

    return lowercase_with_underscores


def create_str_on_line(nr_line, start_column, end_column, matrix):
    s = ""
    if start_column < end_column:
        for i in range(start_column, end_column):
            s += matrix[nr_line][i]
    else:
        for i in range(start_column, end_column, -1):
            s += matrix[nr_line][i]
    return s


def create_str_on_column(nr_column, start_line, end_line, matrix):
    s = ""
    if start_line < end_line:
        for i in range(start_line, end_line):
            s += matrix[i][nr_column]
    else:
        for i in range(start_line, end_line, -1):
            s += matrix[i][nr_column]
    return s


def ex_5(matrix_of_chars):
    """

    :param matrix_of_chars:
    :return: the string that you get by going through spiral order in the matrix
    """
    n = len(matrix_of_chars)
    start_i = 0
    start_j = 0
    end_i = n
    end_j = n
    final_string = ""
    while start_i < end_i and start_j < end_j:
        #  print(f"start_i={start_i}\nend_i={end_i}\nstart_j={start_j}\nend_j={end_j}")
        if start_j < end_j:
            final_string += create_str_on_line(start_i, start_j, end_j, matrix_of_chars)  # print the first line
        if start_i + 1 < end_i:
            final_string += create_str_on_column(end_j - 1, start_i + 1, end_i,
                                                 matrix_of_chars)  # print the last column
        if end_j - 2 > start_i - 1:
            final_string += create_str_on_line(end_i - 1, end_j - 2, start_i - 1,
                                               matrix_of_chars)  # print the bottom line
        if end_i - 2 > start_i:
            final_string += create_str_on_column(start_j, end_i - 2, start_i, matrix_of_chars)  # print the first column
        start_i += 1
        end_i -= 1
        start_j += 1
        end_j -= 1

    return final_string


def ex_6(number):
    """

    :param number:
    :return: True if is palindrome, False otherwise
    """
    str_number = str(number)
    # print(str_number[-1::-1])  from end to the first char, with step -1
    return str_number == str_number[::-1]


def ex_7(string):
    """
    Extracts the first number from a string ( Ex : "An apple is 123 USD", this function will return 123)
    :param string:
    :return: the (float) number which is found or None (if it doesn't contain digits)
    """

    number_string = ""
    number_started = False
    has_dot = False
    for char in string:
        if char.isdigit():
            number_started = True
            number_string += char

        elif number_started and char == "." and (not has_dot):
            number_string += char
            has_dot = True

        elif (not number_started) and (char == "+" or char == "-"):
            number_string += char
            number_started = True
        else:
            if number_started:  # there has already been found a number
                return float(number_string)

    return None  # no digit was found


def ex_8(number):
    """
    count how many bits of 1 :param number: has
    :param number:
    :return: the number of bits of 1
    """
    ct = 0
    while number > 0:
        ct += number & 0b1
        number >>= 1

    return ct


def ex_9(string):
    """
    Determines the mose common letter in a string, and return a tuple ( [], int ) where the list will
    contain the letters that apper the most and the number will represent the number of times that the character
    appears
    :param string:
    :return: (list[], number)
    """

    dict_letters = {}

    max_appears = 0
    for char in string:
        if char.isalpha():
            if char in dict_letters:
                dict_letters[char] += 1
                if max_appears < dict_letters[char]:
                    max_appears = dict_letters[char]

            else:
                dict_letters[char] = 1
                if max_appears < dict_letters[char]:
                    max_appears = dict_letters[char]

    list_max_letters = []

    for key in dict_letters:
        if dict_letters[key] == max_appears:
            list_max_letters.append(key)

    return list_max_letters, max_appears


def ex_10(string):
    """
    Counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space
    :param string:
    :return: the number of words in a sentence
    """
    return len(string.split(" "))


print("-----------EX_1-----------")
print(ex_1())
print("-----------EX_2-----------")
print(ex_2("ThE number of Vowels is : 7 "))
print("-----------EX_3-----------")
print(ex_3("hellohelloshello hello hello", "hello"))
print(ex_3("aaaa","aaa"))
print("-----------EX_4-----------")
print(ex_4("upperCamelCase"))

cool_matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]
cool_matrix_numbers_1 = [
    ['1', '-', '3', '-', '5', '-'],
    ['-', '21', '-', '23', '-', '7'],
    ['19', '-', '33', '-', '25', '-'],
    ['-', '31', '-', '35', '-', '9'],
    ['17', '-', '29', '-', '27', '-'],
    ['-', '15', '-', '13', '-', '11']

]
cool_matrix_numbers_2 = [
    ['0', '-', '2', '-', '4'],
    ['-', '16', '-', '18', '-'],
    ['14', '-', '24', '-', '6'],
    ['-', '22', '-', '20', '-'],
    ['12', '-', '10', '-', '8']

]
print("-----------EX_5-----------")
print(ex_5(cool_matrix))
print(ex_5(cool_matrix_numbers_1))
print(ex_5(cool_matrix_numbers_2))
print(ex_5(['1']))

print("-----------EX_6-----------")
print(f"534726 is palindrome : {ex_6(534726)}")
print(f"123321 is palindrome : {ex_6(123321)}")
print(f"0 is palindrome : {ex_6(0)}")
print(f"111111111 is palindrome : {ex_6(111111111)}")

print("-----------EX_7-----------")
print(f"The first number in 'Hello ; 2020 ; 21' is : {ex_7('Hello ; 2020 ; 21')}")
print(f"The first number in '0.123131 ; -23 ; DONE' is : {ex_7('0.123131 ; -23 ; DONE')}")
print(f"The first number in '+23 ; -23 ; DONE' is : {ex_7('+23 ; -23 ; DONE')}")
print(f"The first number in ' Hello -23.010123 ; -23 ; DONE 1-' is : {ex_7(' Hello -23.010123 ; -23 ; DONE 1-')}")
print(f"The first number in ' Nooo numberrrrr' is : {ex_7(' Nooo numberrrrr')}")


print("-----------EX_8-----------")
print(f"number 0 has : {ex_8(0)} bits of 1")
print(f"number 2**6({bin(2**6)}) has : {ex_8(2**4)} bits of 1")
print(f"number 2**3-1({bin(2**3-1)}) has : {ex_8(2**3-1)} bits of 1")
print(f"number 24({bin(24)}) has : {ex_8(24)} bits of 1")

print("-----------EX_9-----------")
print(f"The string is 'Hello How are you 121 ' : {ex_9('Hello How are you 121 ')}")
print(f"The string is 'an apple is  not a tomato      ' : {ex_9('an apple is  not a tomato      ')}")
print(f"The string is 'aaa AAA bbb CCC 1111 lll' : {ex_9('aaa AAA bbb CCC 1111 lll')}")

print("-----------EX_10-----------")
print(f"The nr of words in 'I have Python exam' : {ex_10('I have Python exam')}")
print(f"The nr of words in 'This is a sentence with more words than the last one' : {ex_10('This is a sentence with more words than the last one')}")






