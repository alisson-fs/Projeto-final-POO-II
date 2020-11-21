import pygame
from tela import Tela


class Fase:

    def __init__(self,
                 bg: object,
                 elements: list,
                 tela: Tela):

        self.__bg = bg
        self.__elements = elements
        self.__tela = tela

    def blitme(self):
        self.__tela.display.blit(self.__bg, (0, 0))
        for i in self.__elements:
            i.blitme()

    def update(self):
        for i in self.__elements:
            i.update()
