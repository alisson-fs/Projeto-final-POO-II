from texto import Texto
from velocidade_controller import VelocidadeController

class Pontuacao:
    def __init__(self, pontos, tela, cor, fundo):
        self.__pontos = pontos
        self.__tela = tela
        self.__cor = cor
        self.__WHITE = (255, 255, 255)
        self.__texto = Texto("", "Materials/Early GameBoy.ttf", 25, self.__cor, self.__tela, [370, 10])

        self.__timer = 0
        self.__timerMax = 30
        self.__timerAtual = self.__timerMax
        self.__velocidade_controller = VelocidadeController()
        self.__len_pontuacao = 1
        self.__fundo = fundo

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, pontos):
        self.__pontos = pontos

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade):
        self.__velocidade = velocidade

    def draw(self):
        self.__texto.texto = str(self.__pontos)
        self.__texto.draw()

    def update(self):
        self.__timerAtual = self.__timerMax / self.__velocidade_controller.vel_atual
        self.__timer += 1
        if self.__timer > self.__timerAtual:
            self.__timer = 0
            self.__pontos += 1
        self.ajuste_pontos()

    def ajuste_pontos(self):
        if self.__len_pontuacao < len(str(self.__pontos)):
            self.__texto.posicao[0] += -25
            self.__len_pontuacao += 1

            if len(str(self.__pontos)) >=2:
                self.__fundo.update_width(25)

    def zerar(self):
        self.__velocidade_controller.zerar()
        self.pontos = 0
        self.__len_pontuacao = 1
        self.__texto.posicao = [370, 10]
        self.__fundo.param = [360, 10, 35, 30]
