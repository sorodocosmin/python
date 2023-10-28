def convert_list_to_tuple(elem_list):
    """
    a list can have list of lists
    :param elem_list:
    :return:
    """
    if isinstance(elem_list, list):
        return tuple(convert_list_to_tuple(item_list) for item_list in elem_list)
    else:
        return elem_list


def ex_1(list_a: list, list_b: list) -> list:
    """
    Write a function that receives as parameters two lists a and b
    and returns a list of sets containing:
    (a intersected with b, a reunited with b, a - b, b - a)
    :param list_a:
    :param list_b:
    :return:
    """

    #  won t work if list_a contains a tuple of a list
    set_a = set(convert_list_to_tuple(list_a))
    set_b = set(convert_list_to_tuple(list_b))

    return [set_a.intersection(set_b), set_a.union(set_b), set_a.difference(set_b), set_b.difference(set_a)]


def ex_2(string: str) -> dict:
    """
    Counts the number of chars in that string and returns a dictionary
    :param string:
    :return:
    """
    counter_dict = {}
    for char in string:
        if char in counter_dict:
            counter_dict[char] += 1
        else:
            counter_dict[char] = 1

    return counter_dict


def ex_3(dict_1, dict_2) -> bool:
    """
    Compare two dictionaries without using the operator "==" returning True or False.
    (Attention, dictionaries must be recursively covered because they can contain other
    containers, such as dictionaries, lists, sets, etc.)
    :param dict_1:
    :param dict_2:
    :return:
    """
    if type(dict_1) is not type(dict_2):
        return False

    elif isinstance(dict_1, dict):
        if len(dict_1.keys()) != len(dict_2.keys()):
            return False

        # now, we need to check that every key in dict_1 is found is dict_2
        for item in dict_1.items():
            if item[0] not in dict_2:
                return False
            else:
                value_1 = item[1]
                value_2 = dict_2[item[0]]
                res = ex_3(value_1, value_2)
                if res is False:
                    return False

        # if every value of the dict are equal -> return True
        return True

    elif isinstance(dict_1, set) or isinstance(dict_1, frozenset):
        if len(dict_1) != len(dict_2):
            return False

        # knowing that sets can only contain hashable types we can only use == (dict is not a hashable type)
        return dict_1 == dict_2

    elif isinstance(dict_1, list) or isinstance(dict_1, tuple):
        if len(dict_1) != len(dict_2):
            return False

        # 2 lists or tuples are equal if on every pos there are the same elements
        for i in range(len(dict_1)):
            res = ex_3(dict_1[i], dict_2[i])
            if res is False:
                return False

        # if we finished the entire lists/ tuples
        return True

    else:  # for the other type(int, float, complex, str, bool, NoneType) is sufficient to compare then with ==
        return dict_1 == dict_2


def ex_4(tag: str, content: str, **kwargs) -> str | None:
    """
    The build_xml_element function receives the following parameters: tag, content, and key-value elements
    given as name-parameters.
    Build and return a string that represents the corresponding XML element.
    Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
    returns  the string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"
    :param tag:
    :param content:
    :param kwargs:
    :return:
    """

    if type(tag) is not str or type(content) is not str:
        return None

    string_tag = "<" + tag + " "

    for args in kwargs.items():
        if type(args[1]) is str:
            string_tag += args[0] + "=\"" + args[1] + "\" "
        else:
            string_tag += args[0] + "=" + str(args[1]) + " "

    string_tag = string_tag[:-1]  # remove the last space
    string_tag += "> " + content + " </" + tag + ">"

    return string_tag


def ex_5(set_rules: set, dictionary_to_be_checked: dict) -> bool:
    """
    set_rules is formed by tuples as follows:
    (key, prefix_value, middle_value, suffix_value)
    key -> every key o the dict needs to be in the set_rules (set_rules can have more keys than the dict)
    prefix_value -> the value needs to start with the prefix
    middle_value -> the value needs to have middle_value, but not starrt with id or end
    suffix_value -> ..
    :param set_rules:
    :param dictionary_to_be_checked:
    :return:
    """

    nr_keys_from_rules_found_in_dict = 0

    for rule in set_rules:
        if rule[0] in dictionary_to_be_checked:
            nr_keys_from_rules_found_in_dict += 1
            value = dictionary_to_be_checked[rule[0]]
            if type(value) is not str:
                return False

            if len(value) <= 2 and len(rule[2]) >= 1:
                return False

            if len(rule[2]) >= 1:
                if rule[2] not in value[1:-1]:
                    return False

            if not (value.startswith(rule[1]) and value.endswith(rule[3])):
                return False

    if nr_keys_from_rules_found_in_dict != len(dictionary_to_be_checked):  # if dict contain a key that is not in set_rules
        return False

    return True


def ex_6(list_nr: list) -> tuple:
    """
    returns a tuple (a, b), representing the number of unique elements in the list,
    and b representing the number of duplicate elements in the list (use sets to achieve this objective)
    :param list_nr:
    :return:
    """

    set_nr = set(list_nr)
    return len(set_nr), len(list_nr) - len(set_nr)


def ex_7(*list_sets) -> dict:
    """
    a variable number of sets and returns a dictionary with the following operations from all sets two by two:
    reunion, intersection, a-b, b-a.
    The key will have the following form: "a op b", where a and b are two sets,
    and op is the applied operator: |, &, -.
    :param list_sets:
    :return:
    """

    dict_sets_operations = {}

    for i, el_set_1 in enumerate(list_sets):
        for j, el_set_2 in enumerate(list_sets):
            if i < j:  # it won t appear a & b = .. and also b & a
                dict_sets_operations[str(el_set_1) + " & " + str(el_set_2)] = el_set_1.intersection(el_set_2)
                # if 2 sets don t have common elements, it will be inserted set() and not {}
                dict_sets_operations[str(el_set_1) + " | " + str(el_set_2)] = el_set_1.union(el_set_2)
                dict_sets_operations[str(el_set_1) + " - " + str(el_set_2)] = el_set_1.difference(el_set_2)
                dict_sets_operations[str(el_set_2) + " - " + str(el_set_1)] = el_set_2.difference(el_set_1)

    return dict_sets_operations


def ex_10(mapping: dict) -> list:
    """
    This dictionary always contains a string key "start".
    Starting with the value of this key you must obtain a list of objects by iterating over mapping
    in the following way: the value of the current key is the key for the next value,
    until you find a loop (a key that was visited before).
    :param mapping:
    :return:
    """
    next_key = mapping['start']
    list_values = []
    dict_visited = {}

    while next_key not in dict_visited:
        list_values += [next_key]
        dict_visited[next_key] = True
        next_key = mapping[next_key]

    return list_values


def ex_11(*list_args, **kwargs):
    """
    Write a function that receives a variable number of positional arguments and a variable number of keyword arguments
    and will return the number of positional arguments whose values can be found among keyword arguments values
    :param list_args:
    :param kwargs:
    :return:
    """
    # won t work if we have list of list of lists as 1 arg ... etc

    nr = 0
    for elem in list_args:
        if elem in kwargs.values():
            nr += 1

    return nr
