from estado import Estado
from events_pausa import EventsPausa
from texto import Texto
from fundo import Fundo
from botao import Botao

class EstadoPausa(Estado):
    def __init__(self, pontuacao):
        super().__init__()
        self.__events_pausa = EventsPausa()
        self.__pontuacao = pontuacao
        
        self.__texto_pausado = Texto("Pausado", "Materials/Early GameBoy.ttf", 50, self.BLACK, self.tela, [30, 70])
        
        self.__texto_continuar = Texto("Continuar", "Materials/Early GameBoy.ttf", 40, self.WHITE, self.tela, [25, 210])
        self.__fundo_continuar = Fundo([20, 200, 360, 70], self.WHITE, self.tela)
        self.__botao_continuar = Botao(self.__texto_continuar, self.__fundo_continuar, self.GREEN, self.DARK_GREEN, self.__events_pausa)
        
        self.__texto_menu = Texto("Menu", "Materials/Early GameBoy.ttf", 40, self.WHITE, self.tela, [125, 310])
        self.__fundo_menu = Fundo([20, 300, 360, 70], self.WHITE, self.tela)
        self.__botao_menu = Botao(self.__texto_menu, self.__fundo_menu, self.GREEN, self.DARK_GREEN, self.__events_pausa)
        
        self.__texto_opcoes = Texto("Opcoes", "Materials/Early GameBoy.ttf", 40, self.WHITE, self.tela, [85, 410])
        self.__fundo_opcoes = Fundo([20, 400, 360, 70], self.WHITE, self.tela)
        self.__botao_opcoes = Botao(self.__texto_opcoes, self.__fundo_opcoes, self.GREEN, self.DARK_GREEN, self.__events_pausa)

    def start(self):
        #Updates
        self.__events_pausa.check_events()
        continuar = self.__botao_continuar.update()
        menu = self.__botao_menu.update()
        opcoes = self.__botao_opcoes.update()

        #Draws
        self.tela.fill(self.GREY)
        self.__texto_pausado.draw()
        self.__botao_continuar.draw()
        self.__botao_menu.draw()
        self.__botao_opcoes.draw()

        if self.__events_pausa.pausa or continuar:
            return 1
        elif menu:
            self.__pontuacao.zerar()
            return 0
        elif opcoes:
            return 3
        else:
            return 2