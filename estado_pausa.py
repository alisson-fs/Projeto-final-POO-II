from estado import Estado
from events_pausa import EventsPausa
from texto import Texto
from fundo import Fundo
from botao import Botao


class EstadoPausa(Estado):
    def __init__(self):
        super().__init__()
        self.__events_pausa = EventsPausa()
        
        self.__texto_pausado = Texto("Pausado", "Materials/Early GameBoy.ttf", 50, self.BLACK, [30, 70])
        
        self.__texto_continuar = Texto("Continuar", "Materials/Retro Gaming.ttf", 40, self.WHITE, [75, 210])
        self.__fundo_continuar = Fundo([20, 200, 360, 70], self.WHITE)
        self.__botao_continuar = Botao(self.__texto_continuar, self.__fundo_continuar, self.GREEN, self.DARK_GREEN, self.__events_pausa)
        
        self.__texto_menu = Texto("Menu", "Materials/Retro Gaming.ttf", 40, self.WHITE, [135, 310])
        self.__fundo_menu = Fundo([20, 300, 360, 70], self.WHITE)
        self.__botao_menu = Botao(self.__texto_menu, self.__fundo_menu, self.GREEN, self.DARK_GREEN, self.__events_pausa)
        
        self.__texto_som = Texto("Som", "Materials/Retro Gaming.ttf", 40, self.WHITE, [150, 410])
        self.__fundo_som = Fundo([20, 400, 360, 70], self.WHITE)
        self.__botao_som = Botao(self.__texto_som, self.__fundo_som, self.GREEN, self.DARK_GREEN, self.__events_pausa)

    def start(self):
        #Updates
        self.__events_pausa.check_events()
        continuar = self.__botao_continuar.update()
        menu = self.__botao_menu.update()
        som = self.__botao_som.update()

        #Draws
        self.tela.fill(self.GREY)
        self.__texto_pausado.draw()
        self.__botao_continuar.draw()
        self.__botao_menu.draw()
        self.__botao_som.draw()

        if self.__events_pausa.pausa or continuar:
            return "jogando"
        elif menu:
            self.pontuacao.zerar()
            self.velocidade_controller.zerar()
            self.fases_controller.zerar()
            return "inicial"
        elif som:
            return "derrota"
        else:
            return "pausa"
