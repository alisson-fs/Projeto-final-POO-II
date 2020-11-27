import pygame
from singleton import Singleton

class SomController(metaclass=Singleton):
    def __init__(self):
        #Inicializa sons
        # sound1 = pygame.mixer.music.load("Nivel1.mp3")
        
        #Lista com os sons
        self.__sounds = []

        #Volume dos sons
        for sound in self.sounds:
            sound.set_volume(0.25)

        #Inicializa as musicas de fundo
        self.__background_music = "Materials/background_sound.mp3"

        #Lista com as musicas de fundo
        self.__musics = [self.__background_music]

    #Toca um som da lista pelo index
    def playSound(self,index):
        pygame.mixer.Sound.play(self.sounds[index])

    #Toca uma musica
    def playMusic(self,index):
        pygame.mixer.music.load(self.musics[index])
        pygame.mixer.music.play(-1)

    #Para a musica atual
    def stopMusic(self):
        pygame.mixer.music.stop()

    @property 
    def sounds(self):
        return self.__sounds
    
    @property
    def background_music(self):
        return self.__background_music
    
    @property
    def musics(self):
        return self.__musics
