class Opcoes:
    def __init__(self,
                 volume_musica: float,
                 volume_efeitos: float,
                 volume_geral: float,
                 dificuldade: str):
        self.__volume_musica = volume_musica
        self.__volume_efeitos = volume_efeitos
        self.__volume_geral = volume_geral
        self.__dificuldade = dificuldade

    @property
    def volume_musica(self):
        return self.__volume_musica

    @volume_musica.setter
    def volume_musica(self, volume_musica):
        self.__volume_musica = volume_musica

    @property
    def volume_efeitos(self):
        return self.__volume_efeitos

    @volume_efeitos.setter
    def volume_efeitos(self, volume_efeitos):
        self.__volume_efeitos = volume_efeitos

    @property
    def volume_geral(self):
        return self.__volume_geral

    @volume_geral.setter
    def volume_geral(self, volume_geral):
        self.__volume_geral = volume_geral

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self.__dificuldade = dificuldade
