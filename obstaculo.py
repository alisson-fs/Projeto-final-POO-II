from animado import Animado
import pygame

class Obstaculo (Animado):
    def __init__(self,
                 posicao: list,
                 nome: str,
                 tela: object,
                 anim: list):
        super().__init__(posicao, nome, tela)
        self.anim = anim
        self.img_atual = self.anim[0]

        self.rect = self.img_atual.get_rect()
        self.pos_inicial()

        self.spriteNum = 0
        self.spriteNumMax = len(self.anim)

        self.spriteTimer = 0
        self.spriteTimerMax = 4


class Obstaculos:        
    def __init__(self):
        self.__obstaculos = []