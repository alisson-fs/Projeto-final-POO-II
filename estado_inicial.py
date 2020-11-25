from estado import Estado
from events_inicial import EventsInicial
from texto import Texto
from fundo import Fundo
from botao import Botao


class EstadoInicial(Estado):
    def __init__(self):
        super().__init__()
        self.__events_inicial = EventsInicial()
        
        self.__nome_jogo1 = Texto("co", "Materials/Early GameBoy.ttf", 25, self.WHITE, self.tela, [50, 100])
        self.__nome_jogo2 = Texto("RUN", "Materials/Early GameBoy.ttf", 40, self.WHITE, self.tela, [100, 85])
        self.__nome_jogo3 = Texto("avirus", "Materials/Early GameBoy.ttf", 25, self.WHITE, self.tela, [215, 100])
        
        self.__texto_play = Texto("PLAY!", "Materials/Early GameBoy.ttf", 75, self.WHITE, self.tela,[30, 400])
        self.__fundo_play = Fundo([25, 410, 360, 70], self.WHITE, self.tela)
        self.__botao_play = Botao(self.__texto_play, self.__fundo_play, self.GREEN, self.DARK_GREEN, self.__events_inicial)

    def start(self):
        #Updates
        self.__events_inicial.check_events()
        play = self.__botao_play.update()

        # Draws
        self.tela.fill(self.GREY)
        self.__nome_jogo1.draw()
        self.__nome_jogo2.draw()
        self.__nome_jogo3.draw()
        self.__botao_play.draw()

        if play:
            return 1
        else:
            return 0
