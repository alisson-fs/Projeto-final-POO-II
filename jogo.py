import pygame
from tela import Tela
from estado_inicial import EstadoInicial
from estado_jogando import EstadoJogando
from estado_pausa import EstadoPausa
from estado_derrota import EstadoDerrota
from estado_recorde import EstadoRecorde
from estado_regras import EstadoRegras
from estado_som import EstadoSom
from estado_developers import EstadoDevelopers


class Jogo:
    def __init__(self):
        # Pygame
        self.__pygame = pygame
        self.__pygame.init()
        self.__pygame.font.init()
        self.__pygame.mixer.init()
        self.__FPS = 30
        self.__FramePerSec = pygame.time.Clock()
        self.__pygame.display.set_caption("coRUNavirus")
        self.__tela = Tela()
        self.__estados = {"inicial": EstadoInicial(),
                          "jogando": EstadoJogando(),
                          "pausa": EstadoPausa(),
                          "derrota": EstadoDerrota(),
                          "recorde": EstadoRecorde(),
                          "regras": EstadoRegras(),
                          "som": EstadoSom(),
                          "developers": EstadoDevelopers()}

    def start(self):
        estado = "inicial"
        while True:
            proximo_estado = self.__estados[estado].start()
            estado = proximo_estado
            self.__tela.update()
            self.__FramePerSec.tick(self.__FPS)
