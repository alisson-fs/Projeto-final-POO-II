from objeto import Objeto

class BGElement(Objeto):

    # (115, 53), (223, 53) 
    # (115, 239), (223, 239)
    # + offset do tamanho

    def __init__(self,
                 posicao: list,
                 nome: str,
                 tela: object,
                 anim: object):
        super().__init__(posicao, nome, tela, anim)

        self.img_atual = self.anim[0]
        self.rect = self.img_atual.get_rect()
        self.pos_inicial()
        
        self.__velocidade = 10

    def update(self):
        self.rect.y += self.__velocidade
        if (self.rect.top >= self.tela.height):
            self.rect.bottom = 0