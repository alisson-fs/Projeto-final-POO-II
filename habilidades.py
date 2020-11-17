from abc import ABC, abstractmethod
from inanimado import Inanimado


class Habilidades(Inanimado, ABC):
    @abstractmethod
    def efeito(self):
        pass
