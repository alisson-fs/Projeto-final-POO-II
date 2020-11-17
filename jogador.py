from objeto import Objeto
import pygame


class Jogador(Objeto):
    def __init__(self,
                 posicao: list,
                 nome: str,
                 tela: object,
                 anim: list):
        super().__init__(posicao, nome, tela, anim)
        self.img_atual = self.anim[0]

        self.rect = self.img_atual.get_rect()
        self.pos_inicial()

        self.spriteNum = 0
        self.spriteNumMax = len(self.anim)

        self.spriteTimer = 0
        self.spriteTimerMax = 4

        self.__velX = 0
        self.__paradas = [35, 145, 260]
        
        self.__meio = True

        #self.__recorde = recorde
        self.__vida_atual = 3
        self.__pontuacao = 0

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, pontuacao):
        self.__pontuacao = pontuacao

    @property
    def vida_atual(self):
        return self.__vida_atual

    @vida_atual.setter
    def vida_atual(self, vida_atual):
        self.__vida_atual = vida_atual

    def move_left(self):
        self.__velX = -10


    def move_right(self):
        self.__velX = 10 

    def blitme(self):

        # Animação
        super().animacao()

        # Desenha na tela
        super().blitme()

    def update(self):
        if self.__meio == False:
            if self.__velX > 0:
                if self.rect.x < self.__paradas[1] and self.rect.x + self.__velX >= self.__paradas[1]:
                    self.__velX = 0
                    self.rect.x = self.__paradas[1]
                    self.__meio = True

            elif self.__velX < 0:
                if self.rect.x > self.__paradas[1] and self.rect.x + self.__velX <= self.__paradas[1]:
                    self.__velX = 0
                    self.rect.x = self.__paradas[1]
                    self.__meio = True

        else:
            if self.rect.x != self.__paradas[1]:
                self.__meio = False
            
        self.rect.x += self.__velX
        self.rect.x = max(min(self.rect.x, self.__paradas[2]), self.__paradas[0])
            