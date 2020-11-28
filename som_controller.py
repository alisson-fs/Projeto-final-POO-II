import pygame
from singleton import Singleton

class SomController(metaclass=Singleton):
    def __init__(self):
        #Inicializa sons
        

        #Lista com os sons
        self.__sounds = []

        #Inicializa as musicas de fundo
        self.__background_music = "Materials/background_sound.mp3"

        #Lista com as musicas de fundo
        self.__musics = [pygame.mixer.music.load(self.__background_music)]
        

    #Toca um som da lista pelo index
    def playSound(self,index):
        pygame.mixer.Sound.play(self.sounds[index])

    #Toca uma musica
    def playMusic(self,index):
        pygame.mixer.music.play(-1)

    def pauseMusic(self):
        pygame.mixer.music.pause()

    #Para a musica atual
    def stopMusic(self):
        pygame.mixer.music.stop()

    #Volume tem que ser float de 0 a 1
    def setVolumeMusic(self, volume):
        pygame.mixer.music.set_volume(volume)

    #Volume tem que ser float de 0 a 1
    def setVolumeSounds(self, volume):
        for sound in self.sounds:
            sound.set_volume(volume)

    @property 
    def sounds(self):
        return self.__sounds
    
    @property
    def background_music(self):
        return self.__background_music
    
    @property
    def musics(self):
        return self.__musics
