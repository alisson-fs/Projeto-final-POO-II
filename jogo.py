import pygame
from pygame.locals import *
from events import Events
from tela import Tela
from jogador import Jogador
from bg_element import BGElement
from fase import Fase
from sound import Sound
from obstaculo_controller import ObstaculoController
from texto import Texto
from pontuacao import Pontuacao
from fundo import Fundo


class Jogo:
    def __init__(self):
        # Pygame
        self.__pygame = pygame
        self.__pygame.init()
        self.__pygame.font.init()
        self.__pygame.mixer.init()
        self.__FPS = 30
        self.__FramePerSec = pygame.time.Clock()
        
        # Atributos gerais
        self.__tela = Tela(pygame)
        self.__velocidade = 100
        self.__jogador = Jogador([145, 450],
                                 "Jogador",
                                 self.__tela,
                                 [pygame.image.load('Materials/p1.png').convert_alpha(self.__tela.tela),
                                  pygame.image.load('Materials/p2.png').convert_alpha(self.__tela.tela),
                                  pygame.image.load('Materials/p1.png').convert_alpha(self.__tela.tela),
                                  pygame.image.load('Materials/p3.png').convert_alpha(self.__tela.tela)],
                                  self.__velocidade)
        self.__events = Events(pygame, self.__jogador)
        self.__sc = Sound()
        
        #Interface gráfica
        self.__borda = pygame.image.load('Materials/borda.png').convert_alpha(self.__tela.tela)
        #self.__bordaVida = Fundo([330, 0, 70, 600], (0,0,0), self.__tela)
        self.__bordaPontos = Fundo([334, 0, 66, 48], (0,0,0), self.__tela)
        self.__pontuacao = Pontuacao(0, self.__tela, self.__velocidade, self.__bordaPontos)
        self.__pygame.display.set_caption("CoRUNavirus")
        
        # Obstáculos
        self.__oc = ObstaculoController(self.__tela, self.__jogador, self.__velocidade)

        # Fase
        self.__bg_1 = pygame.image.load('Materials/AnimatedStreet.png').convert(self.__tela.tela)
        self.__linha_img = pygame.image.load('Materials/AnimatedStreet_Element.png').convert(self.__tela.tela)
        self.__coracao = pygame.image.load("Materials/coracao.png").convert_alpha(self.__tela.tela)

        self.__linha1 = BGElement([115, -53], "", self.__tela, [self.__linha_img], self.__velocidade)
        self.__linha2 = BGElement([230, -53], "", self.__tela, [self.__linha_img], self.__velocidade)
        self.__linha3 = BGElement([115, 292], "", self.__tela, [self.__linha_img], self.__velocidade)
        self.__linha4 = BGElement([230, 292], "", self.__tela, [self.__linha_img], self.__velocidade)
        
        self.__fase_1 = Fase(self.__bg_1, [self.__linha1, self.__linha2, self.__linha3, self.__linha4], self.__tela)

        self.__fases = [self.__fase_1]
        self.__fase_atual = 0


    def start(self):
        # sons
        # self.__sc.playMusic(0)
        while True:

            # Updates
            self.__events.check_events()
            self.__fases[self.__fase_atual].update()
            self.__jogador.update()
            self.__pontuacao.update()
            self.__oc.update()
            self.__oc.timer()
            

            # Draws
            self.__fases[self.__fase_atual].blitme()
            self.__jogador.blitme()
            self.__oc.draw()
            #self.__bordaVida.blitme()
            self.__bordaPontos.blitme()
            self.__pontuacao.draw()
            

            # Draw no numero de vidas
            for i in range(self.__jogador.vida_atual):
                self.__tela.tela.blit(self.__coracao, (350, 100 + 40*i))

            # Desenha borda na tela
            self.__tela.tela.blit(self.__borda, (0, 0))

            # Finaliza ciclo
            self.__tela.update()
            self.__FramePerSec.tick(self.__FPS)
