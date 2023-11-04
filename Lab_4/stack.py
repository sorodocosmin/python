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
            return None
        item = self.__items[-1]
        del self.__items[-1]
        return item

    def peek(self):
        """
        Returns the last item from the stack without removing it
        the changes that you make on the returned item(if it is list, ... etc), it will reflect also in the
        original stack
        :return:
        """
        if len(self.__items) == 0:
            return None

        return self.__items[-1]

    def size(self):
        return len(self.__items)

    def __str__(self):
        return str(self.__items)
