from estado import Estado
from recordes_controller import RecordesController
from botao import Botao
from texto import Texto
from events_recorde import EventsRecorde


class EstadoRecorde(Estado):
    def __init__(self):
        super().__init__()
        self.__events_recorde = EventsRecorde()
        self.__recordes_controller = RecordesController()
        self.__texto_recordes = Texto("Recordes", "Materials/Early GameBoy.ttf", 50, self.BLACK, [5, 40])
        self.__cabecalho_nomes = "Nomes:"
        self.__texto_lista_recordes = [Texto(self.__cabecalho_nomes, "Materials/Retro Gaming.ttf", 10, self.BLACK, [5, 100])]
        for i in range(11):
            self.__texto_lista_recordes.append(Texto(f"{i + 1} - ", "Materials/Retro Gaming.ttf", 10, self.BLACK, [5, 130 + 10 * i]))
        
        '''self.__cabecalho_pontos = "Pontos:"
        self.__texto_lista_recordes = [Texto(self.__cabecalho_pontos, "Materials/Retro Gaming.ttf", 10, self.BLACK, [5, 100])]
        for i in range(11):
            self.__texto_lista_recordes.append(Texto(f"{i + 1} - ", "Materials/Retro Gaming.ttf", 10, self.BLACK, [5, 130 + 10 * i]))'''

        

    def listar_recordes(self):
        recordes = self.__recordes_controller.recordes
        limite = 10
        if len(recordes) < 11:
            limite = len(recordes)
            
        for i in range(limite):
            self.__texto_lista_recordes[i+1].texto = f'{i + 1} - {recordes[i]["nome"]}  {recordes[i]["pontos"]:<15d}'

    def start(self):
        #Updates
        self.__events_recorde.check_events()
        self.listar_recordes()

        #Draws
        self.tela.fill(self.GREY)
        self.__texto_recordes.draw()

        for i in range(10):
            self.__texto_lista_recordes[i].draw()
        
        return "recorde"
