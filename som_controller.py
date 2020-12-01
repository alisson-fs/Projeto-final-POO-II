import pygame
from singleton import Singleton

class SomController(metaclass=Singleton):
    def __init__(self):
        #Inicializa sons
        tosse = "Materials/tosse.mp3"
        respiracao = "Material/respiracao.mp3"

        #Lista com os sons
        self.__sounds = [tosse, respiracao]

        #Inicializa as musicas de fundo
        self.__jogando_music = "Materials/background.mp3"
        self.__derrota_music = "Materials/death.mp3"

        #Lista com as musicas de fundo
        self.__musics = [self.__jogando_music, self.__derrota_music]
        

    #Toca um som da lista pelo index
    def playSound(self,index):
        pygame.mixer.Sound.play(self.sounds[index])

    #Toca uma musica
    def playMusic(self,index):
        pygame.mixer.music.load(self.__musics[index])
        self.setVolumeMusic(0.5)
        pygame.mixer.music.play(-1)

    def pauseMusic(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

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
