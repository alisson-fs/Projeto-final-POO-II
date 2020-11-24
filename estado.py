from abc import ABC, abstractmethod
from tela import Tela

class Estado(ABC):
    def __init__(self):
        self.__tela = Tela()
        self.__GREEN = (0, 100, 0)
        self.__DARK_GREEN = (0, 80, 0)
        self.__WHITE = (255, 255, 255)
        self.__BLACK = (0, 0, 0)
        self.__GREY = (100, 100, 100)
        self.__DARK_GREY = (70, 70, 70)

    @property
    def tela(self):
        return self.__tela

    @property
    def BLACK(self):
        return self.__BLACK

    @property
    def WHITE(self):
        return self.__WHITE

    @property
    def GREEN(self):
        return self.__GREEN

    @property
    def DARK_GREEN(self):
        return self.__DARK_GREEN

    @property
    def GREY(self):
        return self.__GREY

    @property
    def DARK_GREY(self):
        return self.__DARK_GREY

    @abstractmethod
    def start(self):
        pass
