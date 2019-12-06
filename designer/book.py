from errors import *


class Book:

    '''
    Constructor
    @param title
    @param author
    @param publisher
    @param lender
    '''

    def __init__(self, title: str, author: str, publisher: str, lender='': str):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__lender = lender
        self.__available = 1

    '''
    Destructor
    '''

    def __del__(self):
        return

    @classmethod
    def getTitle(self) -> str:
        return self.__title

    @classmethod
    def setTitle(self, title: str) -> None:
        self.__title = title
        return

    @classmethod
    def getAuthor(self) -> str:
        return self.__author

    @classmethod
    def setAuthor(self, author: str) -> None:
        self.__author = author
        return

    @classmethod
    def getPublisher(self) -> str:
        return self.__publisher

    @classmethod
    def setPublisher(self, publisher) -> None:
        self.__publisher = publisher
        return

    @classmethod
    def getAvailable(self) -> int:
        return self.__available

    @classmethod
    def setAvailable(self, status: int) -> None:
        self.__available = status
        return

    @classmethod
    def getLender(self) -> str:
        return self.__lender

    @classmethod
    def setLender(self, lender: str) -> None:
        self.__lender = lender
        return

    @classmethod
    def borrow(self, lender: str):
        try:
            setLender(lender)
            self.setAvailable(0)
            if not self.getAvailable():
                raise BorrowError

        except BorrowError as e:
            print(e)
