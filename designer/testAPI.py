import unittest
from test_api_func import *


class TestAPI(unittest.TestCase):

    def testShowAll(self):
        status_code_showAll = showAll()
        self.assertEqual(status_code_showAll, 200)

    def testShowAvailables(self):
        status_code_showAvailables = showAvailables()
        self.assertEqual(status_code_showAvailables, 200)

    def testShowNotAvailables(self):
        status_code_showNotAvailables = showNotAvailables()
        self.assertEqual(status_code_showNotAvailables, 200)

    def testSearchByTitle(self):
        status_code_searchByTitle = searchByTitle('Power C++')
        self.assertEqual(status_code_searchByTitle, 200)

    def testSearchByAuthor(self):
        status_code_searchByAuthor = searchByAuthor('Eric Freeman')
        self.assertEqual(status_code_searchByAuthor, 200)

    def testSearchByPublisher(self):
        status_code_searchByPublisher = searchByPublisher('Oxford')
        self.assertEqual(status_code_searchByPublisher, 200)

    def testBorrow(self):
        status_code_borrow = borrow('Power C++')
        self.assertEqual(status_code_borrow, 200)

    def testGiveBack(self):
        status_code_giveBack = giveBack('Power C++')
        self.assertEqual(status_code_giveBack, 200)

    def __del__(self):
        print('=' * 50)
        print('Unit Test End')
        print('=' * 50)


if __name__ == '__main__':
    unittest.main()
