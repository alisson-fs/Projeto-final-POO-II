from obstaculo import Obstaculo
from efeito import Efeito
import pygame
import random
from velocidade_controller import VelocidadeController
from tela import Tela
from vacina import Vacina
from mascara import Mascara
from alcool_gel import AlcoolGel

class ObstaculoController:
    def __init__(self, jogador):
        self.__tela = Tela()
        self.__jogador = jogador

        self.__obstaculos_tela = 0
        self.__obstaculos_tela = ["Materials/virus.png", "Materials/EAD.png"]
        self.__pista1 = pygame.sprite.Group()
        self.__pista2 = pygame.sprite.Group()
        self.__pista3 = pygame.sprite.Group()
        self.__efeitos = ["vacina", "mascara", "alcool_gel"]
        self.__pistas = [self.__pista1, self.__pista2, self.__pista3]
        self.__posicoes = [[35, -100], [145, -100], [260, -100]]
        self.__timer_max = 30
        self.__timer = 0
        self.__velocidade_controller = VelocidadeController()
        self.__limite_vel = 10

    def cria_obstaculo(self, qtd):
        for _ in range(qtd):
            pista = random.randint(0, 2)
            if len(self.__pistas[pista]) == 0:
                chance = random.randint(1,2)
                posicao = self.__posicoes[pista]
                
                if chance != 1:
                    image = random.choice(self.__obstaculos_tela)
                    obstaculo = Obstaculo(posicao,
                                [pygame.image.load(image).convert_alpha(self.__tela.display)])
                    self.__pistas[pista].add(obstaculo)
                else:
                    escolhe_efeito = random.choice(self.__efeitos)
                    efeito = None
                    if escolhe_efeito == "vacina":
                        efeito = Vacina(posicao, self.__jogador)
                    elif escolhe_efeito == "mascara":
                        efeito = Mascara(posicao, self.__jogador)
                    elif escolhe_efeito == "alcool_gel":
                        efeito = AlcoolGel(posicao)
                    if efeito != None:
                        self.__pistas[pista].add(efeito)
                    

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
            for obstaculo in pista:
                obstaculo.blitme()

    def update(self):
        for pista in self.__pistas:
            for obstaculo in pista:
                obstaculo.update()

        self.check_colisao()

    def check_colisao(self):
        for i in range(3):
            bateu = pygame.sprite.spritecollideany(self.__jogador, self.__pistas[i])
            #Colisao com obstaculos
            if isinstance(bateu, Obstaculo):
                bateu.kill()
                del bateu

                if not self.__jogador.invencivel:
                    self.__jogador.perde_vida()

            #Colisao com efeitos
            elif isinstance(bateu, Efeito):
                bateu.efeito()
                bateu.kill()
                del bateu

    def zerar(self):
        for pista in self.__pistas:
            pista.empty()
        self.__timer_max = 30
        self.__timer = 0
