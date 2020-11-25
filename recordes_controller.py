from recorde_dao import RecordeDAO


class RecordesController:
    def __init__(self):
        self.__recorde_dao = RecordeDAO()

    def inclui_recorde(self, nome, pontos):
        self.__recorde_dao.add(nome, pontos)

    def exclui_recorde(self, nome, pontos):
        self.__recorde_dao.remove(nome, pontos)

    def buscar_recorde(self, nome, pontos):
        self.__recorde_dao.get(nome, pontos)

    @property
    def recordes(self):
        return self.__recorde_dao.get_all()