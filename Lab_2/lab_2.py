# All functions are tested in the test.py file
def ex_1(n: int) -> list | None:
    """
    The Fibonacci's stream is : 0,1,1,2,3 ...etc
    :param n:
    :return:  a list of the first n Fibonacci terms, None if n is not ok
    """
    if n <= 0:
        return None

    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    list_fibo = [0, 1]
    n -= 2
    while n > 0:
        len_fibo = len(list_fibo)
        list_fibo.append(list_fibo[len_fibo - 1] + list_fibo[len_fibo - 2])
        n -= 1

    return list_fibo


def is_prime(number: int) -> bool:
    """
    The definition of a prime number is any number that has no positive divisors other than itself and the number 1.
    :param number:
    :return:
    """
    if type(number) is not int:  # 11.0 is not a prime number
        return False

    if number <= 1:
        return False

    if number == 2:
        return True

    i = 3
    sqrt_number = int(number ** (1 / 2))
    while i <= sqrt_number:
        if number % i == 0:
            return False
        i += 2

    return True


def ex_2(list_numbers: list) -> list:
    """
    :return:  a list of the prime numbers in the :param list_numbers:
    """

    # return list(filter(lambda nr:
    #                    nr > 1 and len([y for y in range(2, int((nr**(1/2))+1)) if nr % y == 0]) == 0,
    #                    list_numbers))
    # example taken from the course :)
    # for every nr (from list_numbers), it creates a list in which we put numbers
    # from [2; sqrt(nr)+1)] which respect the condition nr % y == 0
    # if nr is a prime number, the list will have no numbers in it

    return list(filter(lambda nr: is_prime(nr), list_numbers))


def ex_3(list_a: list, list_b: list) -> tuple:
    """
    it's worth mentioning the fact that this function can be called with lists, which in theory
    cannot represent a valid set i.e. can have the same value multiple times.
    However, the output of this function will have (for every list of the 4-tuple)
    unique elements (ex: A \cap B won't contain 2 equal elems)
    :param list_a:
    :param list_b:
    :return:
    """
    a_intersected_b = []
    a_minus_b = []
    b_minus_a = []

    for elem_a in list_a:
        if elem_a in list_b:
            if elem_a not in a_intersected_b:
                a_intersected_b += [elem_a]
        else:
            if elem_a not in a_minus_b:
                a_minus_b += [elem_a]

    # we no longer look for elements in B, that are in A (already did that)
    for elem_b in list_b:
        if elem_b not in list_a:
            b_minus_a += [elem_b]

    # the easiest way to have (A \cup B) = (A \cap B) \cup (A\B) \cup (B\A)
    a_reunited_b = a_minus_b + a_intersected_b + b_minus_a

    return a_intersected_b, a_reunited_b, a_minus_b, b_minus_a


def ex_4(list_musical_notes: list, list_steps: list, pos_start: int) -> list | None:
    """
    The function will return the song composed by going through the musical notes
    beginning with the start position and following the moves given as parameter.
    compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
    -->["mi", "fa", "do", "sol", "re"]
    :param list_musical_notes: list(string)
    :param list_steps: list(int)
    :param pos_start: int
    :return:
    """

    len_mus_notes = len(list_musical_notes)

    if pos_start >= len_mus_notes:  # l[len(l)] --> IndexErr
        return None
    elif abs(pos_start) > len_mus_notes:  # l[-len(l)-1] --> IndexErr
        return None

    # we'll no longer check if the list_mus_notes are actually strings and valid notes
    song_composed = [list_musical_notes[pos_start]]
    curr_step = pos_start
    for step in list_steps:
        curr_step += step
        curr_step %= len_mus_notes
        song_composed += [list_musical_notes[curr_step]]

    return song_composed


def ex_5(matrix: list) -> list | None:
    """
    We consider that the param matrix will have the form of a matrix
    :param matrix:
    :return: the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).
    or None if it isn't a square matrix
    """
    size_line_1 = len(matrix[0])
    nr_lines = len(matrix)

    if nr_lines != size_line_1:
        return None

    for lines in matrix:
        if len(lines) != size_line_1:
            return None

    # we create and return a new matrix, as after this function is called the matrix param won't be changed
    new_matrix = []
    for i in range(size_line_1):
        line_new_matrix = []
        for j in range(size_line_1):
            if i > j:
                line_new_matrix += [0]
            else:
                line_new_matrix += [matrix[i][j]]
        new_matrix += [line_new_matrix]

    return new_matrix


# def ex_6(*multiple_lists, nr_of_occurrences: int) -> list | None:
# |-> if the signature of the function had been like this
# we would have had to call it like this :
# ex_6( [1,2],[2,3], nr_of_occurrences = 2)
def ex_6(nr_of_occurrences: int, *multiple_lists) -> list | None:
    """
    It will return None if there is a parameter that is not a list in multiple_lists
    or if nr_of_occurr < 1
    :param multiple_lists:
    :param nr_of_occurrences:
    :return: list containing the items that appear exactly nr_of_occurrences times in the incoming lists
    """

    if nr_of_occurrences < 1:
        return None

    counter = {}

    # knowing that True ~ 1 (and 1 ~ True) and 0 ~ False (and 0 ~ False)
    # ex_1 : a = { 1: 10, True: 2, 0: 13, False: 3} --> when printing a, will print : {1:2, 0:3}
    # ex_2 : a = { True: -2, 1:12, 0: -3, False: 20} --> will print : {True : 12, 0:20}
    # we will use 2 separates variables for keeping count of True and False
    count_True = 0
    count_False = 0
    for list_arg in multiple_lists:
        if type(list_arg) is not list:
            return None
        else:
            for elem in list_arg:
                if elem is True:
                    count_True += 1
                elif elem is False:
                    count_False += 1
                elif elem not in counter:
                    counter[elem] = 1
                else:
                    counter[elem] += 1

    new_list = list(filter(lambda element: counter[element] == nr_of_occurrences,
                           counter.keys()))

    if count_True == nr_of_occurrences:
        new_list += [True]
    if count_False == nr_of_occurrences:
        new_list += [False]

    return new_list


def ex_7(list_numbers: list) -> (int, int):
    """

    :param list_numbers:
    :return: The first element of the tuple will be the number of palindrome numbers
    found in the list and the second element will be the greatest palindrome number.
    if no palindrome number is found, it will return (0, -1)
    """

    # Obs : only positive numbers + 0 have the possibility of being palindrome numbers

    greatest_pal_nr = -1
    nr_pal = 0
    for elem in list_numbers:
        if str(elem) == str(elem)[::-1]:
            if elem > greatest_pal_nr:
                greatest_pal_nr = elem
            nr_pal += 1

    return nr_pal, greatest_pal_nr


def ex_8(list_strings: list, x=1, flag=True):
    """
    Write a function that receives a number x, default value equal to 1,
    a list of strings, and a boolean flag set to True.
    For each string, generate a list containing the characters that have the
    ASCII code divisible by x if the flag is set to True,
    otherwise it should contain characters that have the ASCII code not divisible by x.
    :param list_strings:
    :param x:
    :param flag:
    :return: None if x = 0
    """

    if x == 0:
        return None

    list_of_lists = []

    # Note_1 : if the i-th string doesn't contain any char that respects the rules, an empty list will be added
    # Note_2 : if there are n chars in a string that respect the rule, it will be added n times (in the final result)

    for string in list_strings:
        list_chars = []
        for char in string:
            if (ord(char) % x == 0) is flag:
                list_chars += [char]

        list_of_lists += [list_chars]

    return list_of_lists


def ex_9(matrix):
    """
    Write a function that receives as parameter a matrix which represents
    the heights of the spectators in a stadium and will return a list of tuples
    (line, column) each one representing a seat of a spectator which can't see the game.
    A spectator can't see the game if there is at least one taller spectator standing
    in front of him. All the seats are occupied. All the seats are at the same level.
    Row and column indexing starts from 0, beginning with the closest row from the field.

    We'll consider that all matrix given are valid ( list of lists of positive numbers(>0))

    :param matrix:
    :return:
    """

    max_length_row = max(len(row) for row in matrix)
    nr_rows = len(matrix)
    list_people_that_cannot_see = []

    for j in range(max_length_row):
        max_size = 0
        for i in range(nr_rows):
            if j < len(matrix[i]):  # it might be rows that are not equal
                if matrix[i][j] > max_size:
                    max_size = matrix[i][j]
                elif matrix[i][j] <= max_size:  # the person cannot see the field
                    list_people_that_cannot_see += [(i, j)]

    return list_people_that_cannot_see


def ex_10(*multiple_lists):
    """
    Write a function that receives a variable number of lists and
    returns a list of tuples as follows: the first tuple contains the first items
    in the lists, the second element contains the items on the position 2 in the lists, etc.
    :param multiple_lists:
    :return:
    """

    max_length_list = max(len(lis) for lis in multiple_lists)

    for list_arg in multiple_lists:
        if len(list_arg) < max_length_list:
            list_to_be_added = [None] * (max_length_list - len(list_arg))
            list_arg += list_to_be_added

    return list(zip(*multiple_lists))


def ex_11(list_tuples):
    """
    will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
    Example: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
    :param list_tuples:
    :return:
    """

    # Note_1 : the function does not return anything, it only sorts the given list of tuples
    # Note_2 : if a tuple doesn't have 2 string or the 3-th char of the second string,
    # it will be put in front of those who have (in the final res, when sorting)

    list_tuples.sort(key=lambda elem: "" if (len(elem) <= 1 or len(elem[1]) < 3) else elem[1][2])


def ex_12(list_of_words: list) -> list | None:
    """
    If there is an element in list_of_words that isn't of type string, it will return None
    :param list_of_words:
    :return: return a list of lists of words, grouped by rhyme.
    Two words rhyme if both of them end with the same 2 letters.
    """

    last_2_letters_dict = {}
    for word in list_of_words:
        if type(word) is not str:
            return None
        new_word = word.strip()
        if len(new_word) >= 2:
            last_letter = new_word[-2:]
            if last_letter not in last_2_letters_dict:
                last_2_letters_dict[last_letter] = [word]
            else:
                last_2_letters_dict[last_letter] += [word]

    list_rhythm = [i for i in last_2_letters_dict.values()]

    return list_rhythm
