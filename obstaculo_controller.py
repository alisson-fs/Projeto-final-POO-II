from obstaculo import Obstaculo
import pygame
import random


class ObstaculoController:
    def __init__(self, tela, player, velocidade):
        self.__tela = tela
        self.__player = player
        self.__velocidade = velocidade

        self.__obstaculos_tela = 0
        self.__pista1 = pygame.sprite.Group()
        self.__pista2 = pygame.sprite.Group()
        self.__pista3 = pygame.sprite.Group()
        self.__pistas = [self.__pista1, self.__pista2, self.__pista3]
        self.__posicoes = [[35, -100], [145, -100], [260, -100]]
        # 35, 145, 260

        self.__timer_max = 25
        self.__timer = 0

    def cria_obstaculo(self, qtd):
        for i in range(qtd):
            pista = random.randint(0, 2)
            if len(self.__pistas[pista]) == 0:
                self.__pistas[pista].add(Obstaculo(self.__posicoes[pista],
                                                   "",
                                                   self.__tela,
                                                   [pygame.image.load('Materials/virus.png').convert_alpha(self.__tela.tela)],
                                                   self.__velocidade))

    def timer(self):
        self.__timer += 1
        if self.__timer > self.__timer_max:
            self.cria_obstaculo(random.randint(1, 2))
            self.__timer = 0

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
