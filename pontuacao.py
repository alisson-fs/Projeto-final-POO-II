from texto import Texto


class Pontuacao:
    def __init__(self, pontos, tela, velocidade):
        self.__pontos = pontos
        self.__tela = tela
        self.__BLACK = (0, 0, 0)
        self.__WHITE = (255, 255, 255)
        self.__texto = Texto("", "Materials/Early GameBoy.ttf",
                             25, self.__WHITE, self.__tela, [375, 10])

        self.__timer = 0
        self.__timerMax = 30
        self.__timerAtual = self.__timerMax
        self.__velocidade = velocidade
        self.__len_pontuacao = 1

    def draw(self):
        self.__texto.texto = str(self.__pontos)
        self.__texto.draw()

    def update(self):
        self.__timerAtual = self.__timerMax / self.__velocidade
        self.__timer += 1
        if self.__timer > self.__timerAtual:
            self.__timer = 0
            self.__pontos += 1
        self.ajuste_pontos()

    def ajuste_pontos(self):
        if self.__len_pontuacao < len(str(self.__pontos)):
            self.__texto.posicao[0] += -25
            self.__len_pontuacao += 1


        # if len(str(self.__pontos)) > 2:
        #     self.__texto.posicao[0] += (len(str(self.__pontos)) - 1) * 25
