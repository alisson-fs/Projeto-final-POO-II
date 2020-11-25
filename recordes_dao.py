import pickle


class RecordeDAO:
    def __init__(self,
                 datasource='recordes.pkl'):
        self.__datasource = datasource
        self.__object_cache = []
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        data = open(self.__datasource, 'wb')
        pickle.dump(self.__object_cache, data)
        data.close()

    def __load(self):
        data = open(self.__datasource, 'rb')
        self.__object_cache = pickle.load(data)
        data.close()

    def add(self, nome, pontos):
        self.__object_cache.append({"nome": nome, "pontos": pontos})
        self.__dump()

    def remove(self, nome, pontos):
        for recorde in self.__object_cache:
            if recorde["nome"] == nome and recorde["pontos"] == pontos:
                self.__object_cache.remove(recorde)
        self.__dump()

    def get(self, nome, pontos):
        for recorde in self.__object_cache:
            if recorde["nome"] == nome and recorde["pontos"] == pontos:
                return recorde

    def get_all(self):
        return self.__object_cache

    def remove_all(self):
        self.__object_cache = []
        self.__dump()