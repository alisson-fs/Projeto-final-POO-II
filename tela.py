import pygame

class Tela:
    def __init__(self, medidas: tuple):
        self.__medidas = medidas
        self.__display = pygame.display.set_mode(self.__medidas)

    @property
    def display(self):
        return self.__display

    @property
    def width(self):
        return self.__display.get_width()

    @property
    def height(self):
        return self.__display.get_height()

    def update(self):
        pygame.display.update()

    def fill(self, cor):
        self.__display.fill(cor)
