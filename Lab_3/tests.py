import unittest
import lab_03
import random


def list_1_same_list_2(list_1, list_2):
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
    def tests_ex_1(self):
        # different elements example
        a = [1, 2, 3, 4, [-1, -1, [-23]], "34"]
        b = ['34', 3, [-1, -1, [-23]], 23, -1]
        a_cap_b = {"34", 3, (-1, -1, (-23,))}
        a_cup_b = {1, 2, 4, 3, (-1, -1, (-23,)), '34', 23, -1}
        a_min_b = {1, 2, 4}
        b_min_a = {23, -1}
        res_ex_3 = lab_03.ex_1(a, b)
        self.assertEqual(True, list_1_same_list_2(a_cap_b, res_ex_3[0]))
        self.assertEqual(True, list_1_same_list_2(a_cup_b, res_ex_3[1]))
        self.assertEqual(True, list_1_same_list_2(a_min_b, res_ex_3[2]))
        self.assertEqual(True, list_1_same_list_2(b_min_a, res_ex_3[3]))

        # test with random numbers
        # for _ in range(1, 100_000):
        a = set(random.randint(1, 200) for _ in range(100))
        b = set(random.randint(1, 200) for _ in range(100))
        res_ex_3 = lab_03.ex_1(list(a), list(b))
        self.assertEqual(a.intersection(b), set(res_ex_3[0]))
        self.assertEqual(a.union(b), set(res_ex_3[1]))
        self.assertEqual(a.difference(b), set(res_ex_3[2]))
        self.assertEqual(b.difference(a), set(res_ex_3[3]))

    def tests_ex_2(self):
        # empty case
        string = ""
        result = lab_03.ex_2(string)
        self.assertEqual({}, result)

        # single letter
        string = "cc"
        result = lab_03.ex_2(string)
        self.assertEqual({"c": 2}, result)

        # ex given
        string = "Ana has apples."
        result = lab_03.ex_2(string)
        self.assertEqual({'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}, result)

    def tests_ex_3(self):
        # equal dicts
        dict_1 = {'a': 1, 'b': 2, 'c': [1, 2, 3]}
        dict_2 = {'b': 2, 'c': [1, 2, 3], 'a': 1}
        self.assertTrue(lab_03.ex_3(dict_1, dict_2))

        # dicts with value of dicts
        dict_1 = {'a': {'b': {'c': [1, 2, True]}},
                  'b': (0,),
                  'Cosmin': "Sorodoc"
                  }
        dict_2 = {'a': {'b': {'c': [1, 2, True]}},
                  "Cosmin": "Sorodoc",
                  'b': (0,)
                  }
        self.assertTrue(lab_03.ex_3(dict_1, dict_2))

        # dicts with lists of dicts
        dict_1 = {'elem_1': [0, 1, 2, 3, {"dict_in_list": [1+2j, 4, 10]}],
                  'set': {10.12 + 3.1j, True, -1},
                  '': ""
                  }
        dict_2 = {'': '',
                  "set": {True, -1, 10.12 + 3.1j},
                  'elem_1': [0, 1, 2, 3, {"dict_in_list": [1+2j, 4, 10]}]
                  }
        self.assertTrue(lab_03.ex_3(dict_1, dict_2))

        # not equal dicts
        dict_1 = {'elem_1': 1,
                  'elem_2': 2,
                  }
        dict_2 = {'elem_1': '1',
                  'elem_2': 2
                  }
        self.assertFalse(lab_03.ex_3(dict_1, dict_2))

        dict_1 = {'elem_1': {"e1_1": [1, None], "e1_2": (2,)},  # will return Fls because the order in the list differs
                  'elem_2': None,
                  }
        dict_2 = {'elem_1': {"e1_1": [None, 1], "e1_2": (2,)},
                  'elem_2': None
                  }
        self.assertFalse(lab_03.ex_3(dict_1, dict_2))

        dict_1 = {'elem_1': {"e1_1": [None, 1], "e1_2": (2, True, {10, 20, -1.2})},
                  (1, 2, 3): None,
                  }
        dict_2 = {'elem_1': {"e1_1": [None, 1], "e1_2": (2, True, {10, 20, -1.2})},
                  (1, 2, 3): None
                  }
        self.assertTrue(lab_03.ex_3(dict_1, dict_2))

    def tests_ex_4(self):
        # given ex
        result = lab_03.ex_4("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
        expected = '<a href="http://python.org" _class="my-link" id="someid"> Hello there </a>'
        self.assertEqual(expected, result)

        result = lab_03.ex_4("div", "", _class="my-div")
        self.assertEqual('<div _class="my-div">  </div>', result)

    def tests_ex_5(self):
        # ex given
        set_rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
        dictionary = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
        self.assertFalse(lab_03.ex_5(set_rules, dictionary))

        rules = {("key1", "pre", "mid", "suf")}  # it ends with fix
        dictionary = {"key1": "prefixmiddlesuffix"}
        self.assertFalse(lab_03.ex_5(rules, dictionary))

        # empty middle
        rules = {("key1", "pre", "", "suf")}  # it ends with fix
        dictionary = {"key1": "presuf"}
        self.assertTrue(lab_03.ex_5(rules, dictionary))

        # all empty middle
        rules = {("key1", "", "", ""), ("key2", "sa", "l", "ut")}  # it ends with fix
        dictionary = {"key1": "anything", "key2": "salut"}
        self.assertTrue(lab_03.ex_5(rules, dictionary))

        set_rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter"), ("key3", "", "", "")}
        dictionary = {"key1": "come inside, it's too cold out"}
        self.assertTrue(lab_03.ex_5(set_rules, dictionary))

    def tests_ex_6(self):
        list_nr = []
        result = lab_03.ex_6(list_nr)
        self.assertEqual(result, (0, 0))

        # no duplicates
        list_nr = [1, 2, 3, 4, 5]
        result = lab_03.ex_6(list_nr)
        self.assertEqual(result, (5, 0))

        # nr duplicates = nr unique
        list_nr = [1, 1, 2, 2, 3, 3, 4, 4]
        result = lab_03.ex_6(list_nr)
        self.assertEqual(result, (4, 4))

        list_nr = [5, 5, 5, 5]
        result = lab_03.ex_6(list_nr)
        self.assertEqual(result, (1, 3))

    def tests_ex_10(self):
        # ex given
        self.assertEqual(['a', '6', 'z', '2'], lab_03.ex_10({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

    def tests_ex_11(self):
        result = lab_03.ex_11()
        self.assertEqual(0, result)

        # ex given
        result = lab_03.ex_11(1, 2, 3, 4, x=1, y=2, z=3, w=5)
        self.assertEqual(3, result)

        result = lab_03.ex_11(1, 2, 3, 4, x=5, y=6, z=7, w=8)
        self.assertEqual(0, result)


if __name__ == '__main__':
    unittest.main()
