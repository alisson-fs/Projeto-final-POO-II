import pygame
from pygame.locals import *
from events import Events
from tela import Tela
from jogador import Jogador
from bg_element import BGElement
from fase import Fase
from sound import Sound


class Jogo:
    def __init__(self):
        # Objetos Gerais do jogo
        self.__pygame = pygame
        self.__tela = Tela(pygame)
        self.__jogador = Jogador([145, 450],
                                 "Jogador",
                                 self.__tela,
                                 [pygame.image.load('Materials/p1.png').convert_alpha(self.__tela.tela),
                                 pygame.image.load('Materials/p2.png').convert_alpha(self.__tela.tela),
                                 pygame.image.load('Materials/p1.png').convert_alpha(self.__tela.tela),
                                 pygame.image.load('Materials/p3.png').convert_alpha(self.__tela.tela)])
        self.__events = Events(pygame, self.__jogador)
        self.__borda = pygame.image.load('Materials/borda.png').convert_alpha(self.__tela.tela)
        self.__sc = Sound()

        # FPS do jogo
        self.__FPS = 30
        self.__FramePerSec = pygame.time.Clock()

        # Objetos fase 1
        self.__bg_1 = pygame.image.load('Materials/AnimatedStreet.png').convert(self.__tela.tela)
        self.__linha_img = pygame.image.load('Materials/AnimatedStreet_Element.png').convert(self.__tela.tela)
        self.__coracao = pygame.image.load("Materials/coracao.png").convert_alpha(self.__tela.tela)

        self.__linha1 = BGElement([115, -53], "", self.__tela, [self.__linha_img])
        self.__linha2 = BGElement([230, -53], "", self.__tela, [self.__linha_img])
        self.__linha3 = BGElement([115, 292], "", self.__tela, [self.__linha_img])
        self.__linha4 = BGElement([230, 292], "", self.__tela, [self.__linha_img])

        # Fases
        self.__fase_1 = Fase(self.__bg_1, [self.__linha1, self.__linha2, self.__linha3, self.__linha4], self.__tela)

        self.__pygame.init()
        self.__pygame.display.set_caption("CoRUNavirus")

    def soma_ponto(self):
        pontos_atuais = self.__jogador.pontuacao
        self.__jogador.pontuacao = (pontos_atuais + 1)
    
    def start(self):
        # sons
        self.__sc.playMusic(0)
        while True:
            # Updates
            self.__events.check_events()
            self.__fase_1.update()
            self.__jogador.update()

            # Draws
            self.__fase_1.blitme()
            self.__jogador.blitme()
            #Draw na pontuacao
            print(self.__jogador.pontuacao)
            self.soma_ponto()

            #Draw no numero de vidas
            for i in range (self.__jogador.vida_atual):
                self.__tela.tela.blit(self.__coracao, (350, 100 + 40*i ))

            # Desenha borda na tela
            self.__tela.tela.blit(self.__borda, (0, 0))

            # Finaliza ciclo
            self.__tela.update()
            self.__FramePerSec.tick(self.__FPS)
