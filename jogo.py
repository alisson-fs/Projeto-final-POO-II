import pygame
from pygame.locals import *
from events_jogando import EventsJogando
from events_inicial import EventsInicial
from events_pausa import EventsPausa
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


class Jogo:
    def __init__(self):
        # Pygame
        self.__pygame = pygame
        self.__pygame.init()
        self.__pygame.font.init()
        self.__pygame.mixer.init()
        self.__FPS = 30
        self.__FramePerSec = pygame.time.Clock()
        self.__GREEN = (0, 100, 0)
        self.__DARK_GREEN = (0, 80, 0)
        self.__WHITE = (255, 255, 255)
        self.__BLACK = (0, 0, 0)
        self.__GREY = (100, 100, 100)

        # Jogando
        # Atributos gerais
        self.__tela = Tela((400, 600))
        self.__velocidade = 10
        self.__jogador = Jogador([145, 450],
                                 "Jogador",
                                 self.__tela,
                                 [pygame.image.load('Materials/p1.png').convert_alpha(self.__tela.display),
                                  pygame.image.load(
                                      'Materials/p2.png').convert_alpha(self.__tela.display),
                                  pygame.image.load(
                                      'Materials/p1.png').convert_alpha(self.__tela.display),
                                  pygame.image.load('Materials/p3.png').convert_alpha(self.__tela.display)],
                                 self.__velocidade)
        self.__events_jogando = EventsJogando(self.__jogador)
        self.__sc = Sound()

        # Interface gráfica
        self.__borda = pygame.image.load(
            'Materials/borda.png').convert_alpha(self.__tela.display)
        self.__bordaPontos = Fundo(
            [360, 10, 35, 30], self.__GREEN, self.__tela)
        self.__pontuacao = Pontuacao(
            0, self.__tela, self.__velocidade, self.__WHITE, self.__bordaPontos)
        self.__pygame.display.set_caption("coRUNavirus")

        # Obstáculos
        self.__oc = ObstaculoController(
            self.__tela, self.__jogador, self.__velocidade)

        # Fase
        self.__bg_1 = pygame.image.load(
            'Materials/AnimatedStreet.png').convert(self.__tela.display)
        self.__linha_img = pygame.image.load(
            'Materials/AnimatedStreet_Element.png').convert(self.__tela.display)
        self.__coracao = pygame.image.load(
            "Materials/coracao.png").convert_alpha(self.__tela.display)

        self.__linha1 = BGElement(
            [115, -53], "", self.__tela, [self.__linha_img], self.__velocidade)
        self.__linha2 = BGElement(
            [230, -53], "", self.__tela, [self.__linha_img], self.__velocidade)
        self.__linha3 = BGElement([115, 292], "", self.__tela, [
                                  self.__linha_img], self.__velocidade)
        self.__linha4 = BGElement([230, 292], "", self.__tela, [
                                  self.__linha_img], self.__velocidade)

        self.__fase_1 = Fase(self.__bg_1, [
                             self.__linha1, self.__linha2, self.__linha3, self.__linha4], self.__tela)

        self.__fases = [self.__fase_1]
        self.__fase_atual = 0

        # Inicial
        # Atributos gerais
        self.__events_inicial = EventsInicial()
        self.__nome_jogo1 = Texto("co", "Materials/Early GameBoy.ttf", 25, self.__WHITE, self.__tela,
                                     [50, 100])
        self.__nome_jogo2 = Texto("RUN", "Materials/Early GameBoy.ttf", 40, self.__WHITE, self.__tela,
                                     [100, 85])
        self.__nome_jogo3 = Texto("avirus", "Materials/Early GameBoy.ttf", 25, self.__WHITE, self.__tela,
                                     [215, 100])
        
        #self.__texto_botao = Texto("Iniciar", "Materials/Early GameBoy.ttf", 15, self.__WHITE, self.__tela,
        #                             [150, 300])
        self.__texto_play = Texto("PLAY!", "Materials/Early GameBoy.ttf", 75, self.__WHITE, self.__tela,
                                     [30, 400])
        self.__fundo_botao = Fundo([25, 410, 360, 70], self.__WHITE, self.__tela)
        self.__botao_play = Botao(self.__texto_play, self.__fundo_botao, self.__GREEN, self.__DARK_GREEN,
                                self.__events_inicial)

        #Pausado
        self.__texto_pausado = Texto("Pausado", "Materials/Early GameBoy.ttf", 40, self.__BLACK, self.__tela,
                                     [100, 10])

        self.__events_pausa = EventsPausa()

    def game_loop(self):
        estado = 0
        while True:
            if estado == 0:
                temp_estado = self.inicial()
                self.__tela.update()
                self.__FramePerSec.tick(self.__FPS)
            elif estado == 1:
                temp_estado =self.jogando()
                self.__tela.update()
                self.__FramePerSec.tick(self.__FPS)
            elif estado == 2:
                temp_estado = self.pausa()
                self.__tela.update()
                self.__FramePerSec.tick(self.__FPS)
            estado = temp_estado
        

    def start(self):
        self.game_loop()

    def jogando(self):
        #self.__sc.playMusic(0)

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

    def inicial(self):
        #Updates
        self.__events_inicial.check_events()
        inicia = self.__botao_play.update()

        # Draws
        self.__tela.fill(self.__GREY)
        self.__nome_jogo1.draw()
        self.__nome_jogo2.draw()
        self.__nome_jogo3.draw()
        self.__botao_play.draw()

        if inicia:
            return 1
        else:
            return 0

    def pausa(self):
        #Updates
        self.__events_pausa.check_events()


        # Draws
        self.__texto_pausado.draw()

        if self.__events_pausa.pausa:
            return 1
        else:
            return 2
