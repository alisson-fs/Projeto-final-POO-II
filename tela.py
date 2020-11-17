class Tela:
    def __init__(self, pygame):
        self.__pygame = pygame
        self.__tela = pygame.display.set_mode((400, 600))

    @property
    def tela(self):
        return self.__tela

    @property
    def width(self):
        return self.__tela.get_width()

    @property
    def height(self):
        return self.__tela.get_height()

    def update(self):
        self.__pygame.display.update()

    def fill(self, cor):
        self.__tela.fill(cor)
