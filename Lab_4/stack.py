import copy


class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items += [item]

    def pop(self):
        """
        Removes the last item from the stack and returns it
        :return:
        """
        if len(self.__items) == 0:
            raise EmptyStackException("The stack is empty!")

        item = self.__items[-1]
        del self.__items[-1]
        return item

    def peek(self):
        """
        Returns the last item from the stack without removing it
        the changed made on the item, won t affect the stack
        -> need to use deepcopy - inefficient
        :return: item if the stack is not empty
        else raises EmptyStackException
        """
        if len(self.__items) == 0:
            raise EmptyStackException("The stack is empty!")

        type_elem = type(self.__items[-1])
        # return same obj for primitive types
        if type_elem is int or type_elem is float or type_elem is bool or type_elem is str:
            return self.__items[-1]

        return copy.deepcopy(self.__items[-1])

    def size(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)


class EmptyStackException(Exception):
    """
    Raised when the stack is empty, and we try to pop/peek
    """
