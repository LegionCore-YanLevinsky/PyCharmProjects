import unittest


class Author:
    def __init__(self, a_id, name):
        self.__id = a_id
        self.__name = name

    def __str__(self, *args, **kwargs):
        return "id: {}\nname: {}".format(self.__id, self.__name)

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name


class TestAddAuthor(unittest.TestCase):
    def setUp(self):
        pass


author_1 = Author(0, "me")
print(author_1)
