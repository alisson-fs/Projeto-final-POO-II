from estado import Estado
from events_derrota import EventsDerrota
from texto import Texto
from fundo import Fundo
from botao import Botao
from pygame_widgets import TextBox

class EstadoDerrota(Estado):
    def __init__(self, pontuacao):
        super().__init__()
        self.__pontuacao = pontuacao

        self.__insereTexto = TextBox(self.tela.display, 20, 250, 360, 70, fontSize=35,
                  borderColour=(0, 0, 0), textColour=(0, 0, 0), radius=10, borderThickness=5,
                  onSubmit=self.teste, placeholderText="Insira seu nome.")

        self.__texto_recorde = Texto("Insira seu nome e aperte Enter.", 
                                    "Materials/Early GameBoy.ttf", 12, self.BLACK, 
                                    self.tela, [32, 320])

        self.__events_derrota = EventsDerrota(self.__insereTexto)
        
        self.__texto_derrota = Texto("Derrota", "Materials/Early GameBoy.ttf", 50, self.BLACK, self.tela, [30, 40])
        
        self.__fundo_pontuacao = Fundo([20, 130, 360, 70], self.DARK_GREY, self.tela)
        self.__texto_pontuacao = Texto(f"Pontos: {self.__pontuacao.pontos}", "Materials/Early GameBoy.ttf", 20, self.WHITE, self.tela, [30, 150])
        
        
        self.__texto_jogar_novamente = Texto("Jogar novamente", "Materials/Early GameBoy.ttf", 22, self.WHITE, self.tela, [42, 430])
        self.__fundo_jogar_novamente = Fundo([20, 410, 360, 70], self.WHITE, self.tela)
        self.__botao_jogar_novamente = Botao(self.__texto_jogar_novamente, self.__fundo_jogar_novamente, self.GREEN, self.DARK_GREEN, self.__events_derrota)
        
        self.__texto_menu_derrota = Texto("Menu", "Materials/Early GameBoy.ttf", 40, self.WHITE, self.tela, [125, 510])
        self.__fundo_menu_derrota = Fundo([20, 500, 360, 70], self.WHITE, self.tela)
        self.__botao_menu_derrota = Botao(self.__texto_menu_derrota, self.__fundo_menu_derrota, self.GREEN, self.DARK_GREEN, self.__events_derrota)  

    def teste(self):
            print(self.__insereTexto.getText())
            self.__texto_recorde.texto = "Recorde salvo com sucesso!"

    def start(self):
        #Updates
        self.__events_derrota.check_events()
        jogar_novamente = self.__botao_jogar_novamente.update()
        menu_derrota = self.__botao_menu_derrota.update()

        
        #Draws
        self.tela.fill(self.GREY)
        self.__texto_derrota.draw()
        self.__fundo_pontuacao.blitme()

        self.__texto_pontuacao.texto = str(f"Pontos: {self.__pontuacao.pontos}")
        self.__texto_pontuacao.draw()

        self.__insereTexto.draw()
        self.__texto_recorde.draw()

        self.__botao_jogar_novamente.draw()
        self.__botao_menu_derrota.draw()

        if jogar_novamente:
            return 1
        elif menu_derrota:
            return 0
        else:
            return 3