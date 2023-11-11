import copy


class Queue:
    def __init__(self):
        self.__items = []

    def push(self, item):
        type_item = type(item)
        if type_item is int or type_item is float or type_item is bool or type_item is str:
            self.__items += [item]
        else:
            self.__items += [copy.deepcopy(item)]

    def peek(self):
        """
        Returns the first item from the queue without removing it
        it will return a deepcopy of that element -- very inefficient
        :return: item if the queue is not empty
        else raises EmptyQueueException
        """
        if len(self.__items) == 0:
            raise EmptyQueueException("The queue is empty!")

        type_elem = type(self.__items[0])
        # return same obj for primitive types
        if type_elem is int or type_elem is float or type_elem is bool or type_elem is str:
            return self.__items[0]

        # we can have a tuple of list -> we need deepcopy
        return copy.deepcopy(self.__items[0])

    def pop(self):
        """
        Removes the first item from the queue and returns it
        :return:
        """
        if len(self.__items) == 0:
            raise EmptyQueueException("The queue is empty!")

        item = self.__items[0]
        del self.__items[0]
        # no need to use deepcopy as the element is removed from the queue
        return item

    def size(self):
        return len(self.__items)


class EmptyQueueException(Exception):
    """
    Raised when the queue is empty, and we try to pop/peek
    """