from estado import Estado
from events_som import EventsSom
from texto import Texto
from fundo import Fundo
from botao_imagem import BotaoImagem
import pygame
from pygame_widgets import Slider


class EstadoSom(Estado):
    def __init__(self):
        super().__init__()
        self.__texto_som = Texto("Som", "Materials/Early GameBoy.ttf", 50, self.BLACK, [130, 40])
        
        self.__texto_musica = Texto("Volume música:", "Materials/Retro Gaming.ttf", 25, self.WHITE, [20, 150])
        self.__texto_efeitos = Texto("Volume efeitos:", "Materials/Retro Gaming.ttf", 25, self.WHITE, [20, 300])
        
        self.__slider_musica = Slider(self.tela.display, 20, 230, 300, 20, min=0, max=1, step=0.1, handleColour=self.GREEN)
        self.__slider_sons = Slider(self.tela.display, 20, 380, 300, 20, min=0, max=1, step=0.1, handleColour=self.GREEN)
        self.__sliders = [self.__slider_musica, self.__slider_sons]

        self.__events_som = EventsSom(self.__sliders)

        self.__numero_musica = Texto("", "Materials/Retro Gaming.ttf", 25, self.WHITE, [335, 225])
        self.__numero_sons = Texto("", "Materials/Retro Gaming.ttf", 25, self.WHITE, [335, 375])
        
        self.__imagem_botao_voltar = pygame.image.load("Materials/voltar.png").convert_alpha(self.tela.display)
        self.__fundo_voltar = Fundo([20, 510, 70, 70], self.WHITE)
        self.__botao_voltar = BotaoImagem(self.__imagem_botao_voltar, (25, 515), self.__fundo_voltar, self.GREEN, self.DARK_GREEN, self.__events_som)


    def start(self):
        #Updates
        self.__events_som.check_events()
        porcentagem_musica = self.__slider_musica.getValue() * 100
        porcentagem_sons = self.__slider_sons.getValue() * 100
        voltar = self.__botao_voltar.update()

        self.__numero_musica.texto = str(int(porcentagem_musica)) + "%"
        self.__numero_sons.texto = str(int(porcentagem_sons)) + "%"

        self.som_controller.setVolumeMusic(self.__slider_musica.getValue())

        #Draws
        self.tela.fill(self.GREY)
        self.__texto_som.draw()
        self.__texto_musica.draw()
        self.__texto_efeitos.draw()
        self.__slider_musica.draw()
        self.__slider_sons.draw()
        self.__numero_musica.draw()
        self.__numero_sons.draw()
        self.__botao_voltar.draw()

        if voltar:
            return "inicial"
        else:
            return "som"