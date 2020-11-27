from abc import ABC, abstractmethod
from tela import Tela
from pontuacao import Pontuacao
from som_controller import SomController
from velocidade_controller import VelocidadeController
from obstaculo_controller import ObstaculoController
from fases_controller import FasesController
from jogador import Jogador
import pygame


class Estado(ABC):
    def __init__(self):
        self.__tela = Tela()
        self.__jogador = Jogador([pygame.image.load("Materials/p1.png").convert_alpha(self.__tela.display),
                                 pygame.image.load("Materials/p2.png").convert_alpha(self.__tela.display),
                                 pygame.image.load("Materials/p1.png").convert_alpha(self.__tela.display),
                                 pygame.image.load("Materials/p3.png").convert_alpha(self.__tela.display)])
        self.__pontuacao = Pontuacao()
        self.__som_controller = SomController()
        self.__velocidade_controller = VelocidadeController()
        self.__obstaculo_controller = ObstaculoController(self.__jogador)
        self.__fases_controller = FasesController()
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
    def jogador(self):
        return self.__jogador

    @property
    def pontuacao(self):
        return self.__pontuacao

    @property
    def som_controller(self):
        return self.__som_controller

    @property
    def velocidade_controller(self):
        return self.__velocidade_controller

    @property
    def obstaculo_controller(self):
        return self.__obstaculo_controller

    @property
    def fases_controller(self):
        return self.__fases_controller

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
