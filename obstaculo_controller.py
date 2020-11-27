from obstaculo import Obstaculo
import pygame
import random
from velocidade_controller import VelocidadeController
from tela import Tela


class ObstaculoController:
    def __init__(self, player):
        self.__tela = Tela()
        self.__player = player

        self.__obstaculos_tela = 0
        self.__pista1 = pygame.sprite.Group()
        self.__pista2 = pygame.sprite.Group()
        self.__pista3 = pygame.sprite.Group()
        self.__pistas = [self.__pista1, self.__pista2, self.__pista3]
        self.__posicoes = [[35, -100], [145, -100], [260, -100]]
        self.__obstaculos_tela = ['Materials/virus.png']

        self.__timer_max = 30
        self.__timer = 0
        self.__velocidade_controller = VelocidadeController()
        self.__limite_vel = 10

    def cria_obstaculo(self, qtd):
        for _ in range(qtd):
            pista = random.randint(0, 2)
            if len(self.__pistas[pista]) == 0:
                image = self.__obstaculos_tela[random.randint(0, len(self.__obstaculos_tela) - 1)]
                self.__pistas[pista].add(Obstaculo(self.__posicoes[pista],
                                                   "",
                                                   self.__tela,
                                                   [pygame.image.load(image).convert_alpha(self.__tela.display)]))

    def timer(self):
        self.__timer += 1
        if self.__timer > self.__timer_max:
            self.cria_obstaculo(random.randint(1, 2))
            self.__timer = 0
            if self.__timer_max > 15:
                if self.__velocidade_controller.vel_atual >= self.__limite_vel:
                    self.__timer_max -= 1
                    self.__limite_vel += 1

    def draw(self):
        for pista in self.__pistas:
            for i in pista:
                i.blitme()

    def update(self):
        for pista in self.__pistas:
            for i in pista:
                i.update()

        self.check_colisao()

    def check_colisao(self):
        for i in range(3):
            bateu = pygame.sprite.spritecollideany(self.__player, self.__pistas[i])
            if isinstance(bateu, pygame.sprite.Sprite):
                bateu.kill()

    def zerar(self):
        for pista in self.__pistas:
            pista.clear()
        self.__timer_max = 30
        self.__timer = 0
