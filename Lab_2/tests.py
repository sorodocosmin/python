import unittest
import random
import lab_2


def list_1_same_list_2(list_1: list, list_2: list) -> True:
    """
    Checks if all numbers from list_1 are in list_2 and vice-versa
    :param list_1:
    :param list_2:
    :return:
    """
    if len(list_1) != len(list_2):
        return False

    for elem_1 in list_1:  # we check if every elem from list_1 is also in list_2
        if elem_1 not in list_2:
            return False

    return True


class MyTestCase(unittest.TestCase):
    def test_ex_1(self):
        self.assertEqual([0], lab_2.ex_1(1))  # first elem is 0
        self.assertEqual(None, lab_2.ex_1(-1))  # returns None for a invalid integer n
        self.assertEqual([0, 1, 1, 2, 3, 5, 8], lab_2.ex_1(7))

    def tests_ex_2(self):
        list_of_all_stuff = [-1, 0, 1, 2, 101.01, 7, 1.0234, 11, 123, 101, "23", [31, 33], 25]
        self.assertEqual([2, 7, 11, 101], lab_2.ex_2(list_of_all_stuff))
        self.assertEqual([], [])
        self.assertEqual([], lab_2.ex_2([-1, -2, -3, -4, "1", '+13']))

    def tests_ex_3(self):
        # different elements example
        a = [1, 2, 3, 4, [-1, -1, [-23]], "34"]
        b = ['34', 3, [-1, -1, [-23]], 23, -1]
        a_cap_b = ["34", 3, [-1, -1, [-23]]]
        a_cup_b = [1, 2, 4, 3, [-1, -1, [-23]], '34', 23, -1]
        a_min_b = [1, 2, 4]
        b_min_a = [23, -1]
        res_ex_3 = lab_2.ex_3(a, b)
        self.assertEqual(True, list_1_same_list_2(a_cap_b, res_ex_3[0]))
        self.assertEqual(True, list_1_same_list_2(a_cup_b, res_ex_3[1]))
        self.assertEqual(True, list_1_same_list_2(a_min_b, res_ex_3[2]))
        self.assertEqual(True, list_1_same_list_2(b_min_a, res_ex_3[3]))

        # test with random numbers
        # for _ in range(1, 100_000):
        a = set(random.randint(1, 200) for _ in range(100))
        b = set(random.randint(1, 200) for _ in range(100))
        res_ex_3 = lab_2.ex_3(list(a), list(b))
        self.assertEqual(a.intersection(b), set(res_ex_3[0]))
        self.assertEqual(a.union(b), set(res_ex_3[1]))
        self.assertEqual(a.difference(b), set(res_ex_3[2]))
        self.assertEqual(b.difference(a), set(res_ex_3[3]))

    def tests_ex_4(self):
        # example given
        self.assertEqual(["mi", "fa", "do", "sol", "re"], lab_2.ex_4(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

        notes = ["do", "re", "mi", "fa", "sol", "la", "si", "do"]
        len_notes = len(notes)
        steps = [1, 1, 1, len_notes, len_notes, 100, -len_notes-4, 0]
        start_pos = -len_notes
        expected_song = ['do', 're', 'mi', 'fa', 'fa', 'fa', 'do', 'fa', 'fa']

        self.assertEqual(expected_song, lab_2.ex_4(notes, steps, start_pos))

        self.assertEqual(None, lab_2.ex_4(notes, steps, 1_000))
        self.assertEqual(None, lab_2.ex_4(notes, steps, -len_notes-1))

    def tests_ex_5(self):
        # non square matrix
        matrix = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5]
        ]
        self.assertEqual(None, lab_2.ex_5(matrix))

        # small matrix
        self.assertEqual([[1]], lab_2.ex_5([[1]]))

        # regular matrix
        matrix = [
            ["a", 12.23, 'hello', -1],
            ["zero", 0.23, 'salut', False],
            [1, 12.23, '', -1.23],
            [4, True, 6, 'not_zero']
        ]
        exp_matrix =[
            ["a", 12.23, 'hello', -1],
            [0, 0.23, 'salut', False],
            [0, 0, '', -1.23],
            [0, 0, 0, 'not_zero']
        ]
        self.assertEqual(exp_matrix, lab_2.ex_5(matrix))

    def tests_ex_6(self):
        # example given
        self.assertEqual([1, 2, 3],
                         lab_2.ex_6(2,
                                    [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))

        # not ok args
        self.assertEqual(None, lab_2.ex_6(-1, [1, 2, 3], [1, 2]))
        self.assertEqual(None, lab_2.ex_6(1, [1, 2], "1", [1, 0]))

        # all types example
        expected_res = [1, "hi", True, False, 2]
        l1 = [1, 1, True, "hi"]
        l2 = [2, 2, 2, False, False, "hi", "hi"]
        l3 = [True, True, False, "23", 23, 1]
        l4 = ["23", 0]
        self.assertEqual(True, list_1_same_list_2(expected_res, lab_2.ex_6(3, l1, l2, l3, l4)))

        # empty list example
        self.assertEqual([], lab_2.ex_6(10, l1, l2, l3, l4))
        self.assertEqual([], lab_2.ex_6(1, [], [], [], []))

    def tests_ex_7(self):
        # simple ex
        self.assertEqual((10, 9), lab_2.ex_7([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

        # doesn't exist
        self.assertEqual((0, -1), lab_2.ex_7([1311, 34, 45, 900_000]))

        # negative nr
        self.assertEqual((1, 0), lab_2.ex_7([-1, -2, 45, -11, 0]))
        self.assertEqual((0, -1), lab_2.ex_7([-1, -2, 45, -11, -33]))

    def tests_ex_8(self):
        # ex given
        self.assertEqual([['e', 's'], ['e', 'o'], ['a']],
                         lab_2.ex_8(["test", "hello", "lab002"], x=2, flag=False))

        # all should be added
        self.assertEqual([['t', 'e', 's', 't'], ['h', 'e', 'l', 'l', 'o'], ['l', 'a', 'b', '0', '0', '2']],
                         lab_2.ex_8(["test", "hello", "lab002"]))

        # empty lists should be returned as all ASCII codes are div. by 1
        self.assertEqual([[], [], [], []],
                         lab_2.ex_8(["test", "hello", "lab002", "AtoZZ"], flag=False))

        # x = 0 -> should return None
        self.assertEqual(None, lab_2.ex_8(["test", "hello", "lab002"], 0))

    def tests_ex_9(self):
        # ex given
        matrix = [
            [1, 2, 3, 2, 1, 1],
            [2, 4, 4, 3, 7, 2],
            [5, 5, 2, 5, 6, 4],
            [6, 6, 7, 6, 7, 5]
        ]
        expected_res = [(2, 2), (3, 4), (2, 4)]
        self.assertEqual(True, list_1_same_list_2(expected_res, lab_2.ex_9(matrix)))

        # all people see
        matrix = [
            [1, 1, 1, 2],
            [2, 2, 2, 3],
            [3, 3, 3, 4],
            [4, 4, 4, 5]
        ]
        self.assertEqual([], lab_2.ex_9(matrix))

        # different length of rows
        matrix = [
            [1, 1, 1, 1],
            [2, 2, 2, 2, 2, 2, 2],
            [3, 3, 3, 4, 5, 8, 10, 20],
            [4, 4, 4, 5, 5, 10]
        ]
        self.assertEqual([(3, 4)], lab_2.ex_9(matrix))

        matrix = [
            [1, 1, 1, 1, 1, 1, 20, 20, 20],
            [2, 2, 10, 2, 2, 2, 2],
            [3, 3, 3, 4, 5, 8, 10, 20],
            [4, 4, 4, 5, 15, 10],
            [1]
        ]
        expected_res = [(4, 0), (1, 6), (2, 2), (2, 6), (2, 7), (3, 2)]
        self.assertEqual(True, list_1_same_list_2(expected_res, lab_2.ex_9(matrix)))

    def tests_ex_10(self):
        # ex given
        l1 = [1, 2, 3]
        l2 = [5, 6, 7]
        l3 = ["a", "b", "c"]
        self.assertEqual([(1, 5, "a"), (2, 6, "b"), (3, 7, "c")],
                         lab_2.ex_10(l1, l2, l3))

        # unequal lists
        l1 = [1, 2, 3]
        l2 = [True, False]
        l3 = ["a", "b", "c", "d"]
        l4 = [1.1]
        exp_res = [(1, True, "a", 1.1), (2, False, "b", None), (3, None, "c", None), (None, None, "d", None)]
        self.assertEqual(exp_res, lab_2.ex_10(l1, l2, l3, l4))

        l1 = [1, 1]
        l2 = []
        self.assertEqual([(1, None), (1, None)], lab_2.ex_10(l1, l2))

        l1 = []
        l2 = []
        self.assertEqual([], lab_2.ex_10(l1, l2))  # shouldn't return any tuple, as there are no values in lists

    def tests_ex_11(self):
        # given example

        list_tup = [('abc', 'bcd'), ('abc', 'zza')]
        exp_list = [('abc', 'zza'), ('abc', 'bcd')]
        lab_2.ex_11(list_tup)
        self.assertEqual(exp_list, list_tup)

        # tuple without second string and/or 3-th char of 2-nd string
        list_tup = [('abc',), ('abc', 'abb'), ("abc", "zza"), ('hello', 'hi', 'salut')]
        exp_list = [('abc',), ('hello', 'hi', 'salut'), ('abc', 'zza'), ('abc', 'abb')]
        lab_2.ex_11(list_tup)
        self.assertEqual(exp_list, list_tup)

        # should remain the same
        list_tup = [("a",), ("b",), ("c",)]
        exp_list = [("a",), ("b",), ("c",)]
        lab_2.ex_11(list_tup)
        self.assertEqual(exp_list, list_tup)

    def tests_ex_12(self):
        # ex given
        list_words = ['carte', 'arme', 'parte', 'ana', 'banana']
        exp_res = [['ana', 'banana'], ['carte', 'parte'], ['arme']]
        self.assertEqual(True, list_1_same_list_2(exp_res, lab_2.ex_12(list_words)))

        # spaces at the end
        list_words = ['carte   ', 'arme', 'parte', 'ana', 'banana    ']
        exp_res = [['ana', 'banana    '], ['carte   ', 'parte'], ['arme']]
        self.assertEqual(True, list_1_same_list_2(exp_res, lab_2.ex_12(list_words)))

        # spaces at the end + beginning + 1-letter-words
        list_words = [' carte   ', '  te  ', 'parte', ' ana', ' banana    ', '   a   ', 'b']
        exp_res = [[' ana', ' banana    '], [' carte   ', '  te  ', 'parte']]
        self.assertEqual(True, list_1_same_list_2(exp_res, lab_2.ex_12(list_words)))

        # no words rhyme
        list_words = ['buna', 'ziua', 'cosmin', 'sunt', 'eu']
        exp_res = [['buna'], ['ziua'], ['cosmin'], ['sunt'], ['eu']]
        self.assertEqual(True, list_1_same_list_2(exp_res, lab_2.ex_12(list_words)))

        # invalid list of words
        list_words = ["hello", "hallo", 33]
        self.assertEqual(None, lab_2.ex_12(list_words))

if __name__ == '__main__':
    unittest.main()
