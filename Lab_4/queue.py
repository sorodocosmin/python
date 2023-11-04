class Queue:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items += [item]

    def peek(self):
        """
        Returns the first item from the queue without removing it
        if the last item is a list/dict/obj of a class, the changes that you make
        to the peeked item will be reflected in the queue also
        :return:
        """
        if len(self.__items) == 0:
            return None

        return self.__items[0]

    def pop(self):
        """
        Removes the first item from the queue and returns it
        :return:
        """
        if len(self.__items) == 0:
            return None

        item = self.__items[0]
        del self.__items[0]
        return item

    def size(self):
        return len(self.__items)
