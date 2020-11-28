from estado import Estado
from events_jogando import EventsJogando
from tela import Tela
from jogador import Jogador
from fundo import Fundo
from pontuacao import Pontuacao
from obstaculo_controller import ObstaculoController
from fases_controller import FasesController
from botao_imagem import BotaoImagem
import pygame


class EstadoJogando(Estado):
    def __init__(self):
        super().__init__()
        self.__musica = False
        self.__events_jogando = EventsJogando(self.jogador)
        self.__borda = pygame.image.load("Materials/borda.png").convert_alpha(self.tela.display)
        self.__vida = pygame.image.load("Materials/coracao.png").convert_alpha(self.tela.display)
        
        self.__imagem_pausa = pygame.image.load("Materials/pausa.png").convert_alpha(self.tela.display)
        self.__fundo_pausa = Fundo([10, 10, 50, 50], self.WHITE)
        self.__botao_pausa = BotaoImagem(self.__imagem_pausa, [15, 15], self.__fundo_pausa, self.GREEN, self.DARK_GREEN, self.__events_jogando)

    def start(self):
        if not self.__musica:
            #self.som_controller.playMusic(0)
            self.__musica = True
        # Updates
        self.__events_jogando.check_events()
        self.fases_controller.update()
        self.fases_controller.fase_atual.update()
        self.jogador.update()
        self.pontuacao.update()
        self.obstaculo_controller.update()
        self.obstaculo_controller.timer()
        self.velocidade_controller.update()

        pausa_botao = self.__botao_pausa.update()

        # Draws
        self.fases_controller.fase_atual.blitme()
        self.jogador.blitme()
        self.obstaculo_controller.draw()
        self.pontuacao.fundo.blitme()
        self.pontuacao.draw()
        self.__botao_pausa.draw()

        # Draw no numero de vidas
        for i in range(self.jogador.vida_atual):
            self.tela.display.blit(self.__vida, (350, 100 + 40*i))

        # Desenha borda na tela
        self.tela.display.blit(self.__borda, (0, 0))

        if self.__events_jogando.pausa or pausa_botao:
            return "pausa"
        else:
            return "jogando"