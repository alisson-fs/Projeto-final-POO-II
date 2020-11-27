from estado import Estado
from events_inicial import EventsInicial
from texto import Texto
from fundo import Fundo
from botao import Botao


class EstadoInicial(Estado):
    def __init__(self):
        super().__init__()
        self.__events_inicial = EventsInicial()
        
        self.__nome_jogo1 = Texto("co", "Materials/Mario-Kart-DS.ttf", 45, self.WHITE, [12, 100])
        self.__nome_jogo2 = Texto("RUN", "Materials/Mario-Kart-DS.ttf", 60, self.WHITE, [77, 87])
        self.__nome_jogo3 = Texto("avirus", "Materials/Mario-Kart-DS.ttf", 45, self.WHITE, [207, 100])
        
        self.__texto_play = Texto("PLAY", "Materials/Retro Gaming.ttf", 60, self.WHITE, [115, 407])
        self.__fundo_play = Fundo([25, 410, 360, 70], self.WHITE)
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
            return "jogando"
        else:
            return "inicial"
