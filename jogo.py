import pygame
from pygame.locals import *
from events_jogando import EventsJogando
from events_derrota import EventsDerrota
from tela import Tela
from jogador import Jogador
from bg_element import BGElement
from fase import Fase
from sound import Sound
from obstaculo_controller import ObstaculoController
from texto import Texto
from pontuacao import Pontuacao
from fundo import Fundo
from botao import Botao
from estado_inicial import EstadoInicial
from estado_jogando import EstadoJogando
from estado_pausa import EstadoPausa
from estado_derrota import EstadoDerrota
from pygame_widgets import Button
from singleton import Singleton
from velocidade_controller import VelocidadeController


class Jogo:
    def __init__(self):
        # Pygame
        self.__pygame = pygame
        self.__pygame.init()
        self.__pygame.font.init()
        self.__pygame.mixer.init()
        self.__FPS = 30
        self.__FramePerSec = pygame.time.Clock()
        self.__tela = Tela()
        self.__GREEN = (0, 100, 0)
        self.__DARK_GREEN = (0, 80, 0)
        self.__WHITE = (255, 255, 255)
        self.__BLACK = (0, 0, 0)
        self.__GREY = (100, 100, 100)

        # Jogando
        # Atributos gerais
        self.__velocidade_controller = VelocidadeController()
        self.__jogador = Jogador([145, 450],
                                 "Jogador",
                                 self.__tela,
                                 [pygame.image.load("Materials/p1.png").convert_alpha(self.__tela.display),
                                  pygame.image.load("Materials/p2.png").convert_alpha(self.__tela.display),
                                  pygame.image.load("Materials/p1.png").convert_alpha(self.__tela.display),
                                  pygame.image.load("Materials/p3.png").convert_alpha(self.__tela.display)])
        self.__events_jogando = EventsJogando(self.__jogador)
        self.__sc = Sound()

        # Interface gráfica
        self.__borda = pygame.image.load("Materials/borda.png").convert_alpha(self.__tela.display)
        self.__bordaPontos = Fundo([360, 10, 35, 30], self.__GREEN, self.__tela)
        self.__pontuacao = Pontuacao(0, self.__tela, self.__WHITE, self.__bordaPontos)
        self.__pygame.display.set_caption("coRUNavirus")

        # Obstáculos
        self.__oc = ObstaculoController(self.__tela, self.__jogador)

        # Fase
        self.__bg_1 = pygame.image.load("Materials/AnimatedStreet.png").convert(self.__tela.display)
        self.__linha_img = pygame.image.load("Materials/AnimatedStreet_Element.png").convert(self.__tela.display)
        self.__coracao = pygame.image.load("Materials/coracao.png").convert_alpha(self.__tela.display)

        self.__linha1 = BGElement([115, -53], "", self.__tela, [self.__linha_img])
        self.__linha2 = BGElement([230, -53], "", self.__tela, [self.__linha_img])
        self.__linha3 = BGElement([115, 292], "", self.__tela, [self.__linha_img])
        self.__linha4 = BGElement([230, 292], "", self.__tela, [self.__linha_img])

        self.__fase_1 = Fase(self.__bg_1, [
                             self.__linha1, self.__linha2, self.__linha3, self.__linha4], self.__tela)

        self.__fases = [self.__fase_1]
        self.__fase_atual = 0

        # Inicial
        self.__estado_inicial = EstadoInicial()

        #Pausado
        self.__estado_pausa = EstadoPausa(self.__pontuacao)
        
        #Derrota
        self.__estado_derrota = EstadoDerrota(self.__pontuacao)
        
    def game_loop(self):
        estado = 3
        musica = False
        while True:
            if estado == 0:
                temp_estado = self.__estado_inicial.start()
            elif estado == 1:
                if not musica:
                    #self.__sc.playMusic(0)
                    musica = True
                temp_estado = self.jogando()
                self.__velocidade_controller.update()
                #print(self.__velocidade_controller.vel_atual)
            elif estado == 2:
                temp_estado = self.__estado_pausa.start()
            elif estado == 3:
                temp_estado = self.__estado_derrota.start()
            self.__tela.update()
            self.__FramePerSec.tick(self.__FPS)
            estado = temp_estado

    def start(self):
        self.game_loop()

    def jogando(self):
        # Updates
        self.__events_jogando.check_events()
        self.__fases[self.__fase_atual].update()
        self.__jogador.update()
        self.__pontuacao.update()
        self.__oc.update()
        self.__oc.timer()

        # Draws
        self.__fases[self.__fase_atual].blitme()
        self.__jogador.blitme()
        self.__oc.draw()
        self.__bordaPontos.blitme()
        self.__pontuacao.draw()

        # Draw no numero de vidas
        for i in range(self.__jogador.vida_atual):
            self.__tela.display.blit(self.__coracao, (350, 100 + 40*i))

        # Desenha borda na tela
        self.__tela.display.blit(self.__borda, (0, 0))

        if self.__events_jogando.pausa:
            return 2
        else:
            return 1


    def opcoes(self):
        pass

    def recordes(self):
        pass

    def regras(self):
        pass
