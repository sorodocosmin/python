from datetime import datetime


class LibraryItem:
    def __init__(self, name, author):
        self._name = name
        self._author = author
        self._is_borrowed = False
        self._date_borrowed = None
        self._nr_of_times_borrowed = 0

    def someone_borrowed_me(self):
        """
        if the item is already borrowed, return False
        :return:
        """
        if self._is_borrowed:
            return False

        self._is_borrowed = True
        self._date_borrowed = datetime.now()
        self._nr_of_times_borrowed += 1
        return True

    def someone_returned_me(self):
        """
        if the item is not borrowed, return False
        :return:
        """
        if self._is_borrowed is False:
            return False

        self._is_borrowed = False
        self._date_borrowed = None
        return True

    def get_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, name, author, nr_of_pages, nr_of_chapters):
        super().__init__(name, author)
        self.__nr_of_pages = nr_of_pages
        self.__nr_of_chapters = nr_of_chapters
        self.__time_finished_reading = None

    def get_nr_of_pages(self):
        return self.__nr_of_pages

    def someone_returned_me(self, time_finished_reading):
        """
        when returning a book, the user must specify how long it took to read it
        :param time_finished_reading:
        :return:
        """
        if super().someone_returned_me() is False:
            return False

        if self.__time_finished_reading is None:
            self.__time_finished_reading = time_finished_reading
        else:
            self.__time_finished_reading = (self.__time_finished_reading + time_finished_reading) / 2

        return True

    def get_info(self):
        info = ""
        info += f"Book: {self._name} by {self._author}, {self.__nr_of_pages} pages({self.__nr_of_chapters} chapt.) \n"
        info += f"Borrowed: {self._nr_of_times_borrowed} times \n"
        info += f"Average time to read: {self.__time_finished_reading} \n"
        if self._is_borrowed:
            info += f"Currently borrowed, borrowed on {self._date_borrowed} \n"
        else:
            info += "Currently not borrowed \n"

        return info


class Magazine(LibraryItem):
    def __init__(self, title, publisher, nr_of_pages, nr_of_articles):
        super().__init__(title, publisher)
        self.__nr_of_pages = nr_of_pages
        self.__nr_of_articles = nr_of_articles

    def get_info(self):
        info = ""
        info += f"Magazine: {self._name} by {self._author}, {self.__nr_of_pages} pages({self.__nr_of_articles} articles) \n"
        info += f"Borrowed: {self._nr_of_times_borrowed} times \n"
        if self._is_borrowed:
            info += f"Currently borrowed, borrowed on {self._date_borrowed} \n"
        else:
            info += "Currently not borrowed \n"
        return info


class DVD(LibraryItem):
    def __item__(self, title, director, time):
        super().__init__(title, director)
        self.__time = time

    def get_info(self):
        info = ""
        info += f"DVD: {self._name} by {self._author}, {self.__time} minutes \n"
        info += f"Borrowed: {self._nr_of_times_borrowed} times \n"
        if self._is_borrowed:
            info += f"Currently borrowed, borrowed on {self._date_borrowed} \n"
        else:
            info += "Currently not borrowed \n"

        return info


# book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1000, 3)
# book.someone_borrowed_me()
# book.someone_returned_me(2)
# book.someone_returned_me(3)
# print(book.get_info())
